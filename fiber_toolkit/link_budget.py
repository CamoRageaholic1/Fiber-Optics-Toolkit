#!/usr/bin/env python3
"""
Link Budget Calculator
Calculate fiber optic link budgets with FOA-compliant loss values.

Author: David Osisek (CFOt)
Standards: FOA, TIA-568
"""

import click
from rich.console import Console
from rich.table import Table
from typing import Dict


class LinkBudget:
    """
    FOA-compliant link budget calculator.
    """
    
    # FOA Standard Values
    CONNECTOR_LOSS_TYPICAL = 0.75  # dB per mated pair
    CONNECTOR_LOSS_MAX = 1.0       # dB per mated pair
    FUSION_SPLICE_TYPICAL = 0.1    # dB
    FUSION_SPLICE_MAX = 0.3        # dB
    MECHANICAL_SPLICE_TYPICAL = 0.3  # dB
    MECHANICAL_SPLICE_MAX = 0.5    # dB
    SAFETY_MARGIN_MIN = 3.0        # dB
    SAFETY_MARGIN_PREFERRED = 6.0  # dB
    
    # Fiber attenuation (dB/km)
    FIBER_LOSS = {
        'SM': {
            1310: 0.35,
            1550: 0.25,
        },
        'MM': {
            850: 3.0,
            1300: 1.0,
        }
    }
    
    def __init__(
        self,
        tx_power: float,
        rx_sensitivity: float,
        fiber_length: float,
        wavelength: int = 1310,
        fiber_type: str = 'SM',
        connector_count: int = 0,
        splice_count: int = 0,
        connector_loss: float = None,
        splice_loss: float = None,
        fiber_loss: float = None,
        safety_margin: float = 3.0
    ):
        """
        Initialize link budget calculator.
        
        Args:
            tx_power: Transmitter power (dBm)
            rx_sensitivity: Receiver sensitivity (dBm)
            fiber_length: Fiber length (km)
            wavelength: Wavelength (nm)
            fiber_type: 'SM' or 'MM'
            connector_count: Number of connectors
            splice_count: Number of splices
            connector_loss: Custom connector loss (dB), uses FOA typical if None
            splice_loss: Custom splice loss (dB), uses FOA typical if None
            fiber_loss: Custom fiber loss (dB/km), uses standard if None
            safety_margin: Safety margin (dB), 3 dB minimum
        """
        self.tx_power = tx_power
        self.rx_sensitivity = rx_sensitivity
        self.fiber_length = fiber_length
        self.wavelength = wavelength
        self.fiber_type = fiber_type
        self.connector_count = connector_count
        self.splice_count = splice_count
        self.safety_margin = safety_margin
        
        # Use custom or default values
        self.connector_loss = connector_loss or self.CONNECTOR_LOSS_TYPICAL
        self.splice_loss = splice_loss or self.FUSION_SPLICE_TYPICAL
        
        # Get fiber loss
        if fiber_loss:
            self.fiber_loss = fiber_loss
        else:
            self.fiber_loss = self._get_fiber_loss(fiber_type, wavelength)
    
    def _get_fiber_loss(self, fiber_type: str, wavelength: int) -> float:
        """Get standard fiber loss for type and wavelength."""
        if fiber_type not in self.FIBER_LOSS:
            return 0.35  # Default SM @ 1310
        
        wavelengths = self.FIBER_LOSS[fiber_type]
        # Find closest wavelength
        closest = min(wavelengths.keys(), key=lambda x: abs(x - wavelength))
        return wavelengths[closest]
    
    def calculate(self) -> Dict:
        """
        Calculate link budget.
        
        Returns:
            Dictionary with all calculations
        """
        # Power budget
        power_budget = self.tx_power - self.rx_sensitivity
        
        # Losses
        fiber_loss_total = self.fiber_length * self.fiber_loss
        connector_loss_total = self.connector_count * self.connector_loss
        splice_loss_total = self.splice_count * self.splice_loss
        total_loss = fiber_loss_total + connector_loss_total + splice_loss_total
        
        # System Operating Margin
        som = power_budget - total_loss - self.safety_margin
        
        # Status
        if som >= 6.0:
            status = "PASS"
            status_detail = "Excellent margin"
        elif som >= 3.0:
            status = "PASS"
            status_detail = "Good margin"
        elif som >= 0:
            status = "MARGINAL"
            status_detail = "Low margin - monitor"
        else:
            status = "FAIL"
            status_detail = "Insufficient margin"
        
        return {
            'power_budget': power_budget,
            'fiber_loss': fiber_loss_total,
            'connector_loss': connector_loss_total,
            'splice_loss': splice_loss_total,
            'total_loss': total_loss,
            'safety_margin': self.safety_margin,
            'som': som,
            'status': status,
            'status_detail': status_detail,
        }
    
    def print_report(self):
        """Print formatted link budget report."""
        console = Console()
        results = self.calculate()
        
        console.print("\n[bold cyan]Link Budget Analysis (FOA Compliant)[/bold cyan]")
        console.print("="*70)
        
        # Input parameters
        input_table = Table(title="Input Parameters", show_header=False)
        input_table.add_column("Parameter", style="cyan")
        input_table.add_column("Value", style="green")
        
        input_table.add_row("Transmitter Power", f"{self.tx_power:.2f} dBm")
        input_table.add_row("Receiver Sensitivity", f"{self.rx_sensitivity:.2f} dBm")
        input_table.add_row("Available Power Budget", f"{results['power_budget']:.2f} dB")
        input_table.add_row("Fiber Length", f"{self.fiber_length:.2f} km")
        input_table.add_row("Wavelength", f"{self.wavelength} nm")
        input_table.add_row("Fiber Type", self.fiber_type)
        
        console.print(input_table)
        console.print()
        
        # Loss breakdown
        loss_table = Table(title="Loss Breakdown", show_header=True)
        loss_table.add_column("Component", style="cyan")
        loss_table.add_column("Quantity", justify="right", style="yellow")
        loss_table.add_column("Unit Loss", justify="right", style="magenta")
        loss_table.add_column("Total Loss", justify="right", style="red")
        
        loss_table.add_row(
            "Fiber",
            f"{self.fiber_length:.2f} km",
            f"{self.fiber_loss:.2f} dB/km",
            f"{results['fiber_loss']:.2f} dB"
        )
        
        if self.connector_count > 0:
            loss_table.add_row(
                "Connectors",
                str(self.connector_count),
                f"{self.connector_loss:.2f} dB/ea",
                f"{results['connector_loss']:.2f} dB"
            )
        
        if self.splice_count > 0:
            loss_table.add_row(
                "Splices",
                str(self.splice_count),
                f"{self.splice_loss:.2f} dB/ea",
                f"{results['splice_loss']:.2f} dB"
            )
        
        loss_table.add_row(
            "[bold]Total System Loss[/bold]",
            "",
            "",
            f"[bold]{results['total_loss']:.2f} dB[/bold]"
        )
        
        console.print(loss_table)
        console.print()
        
        # Margin analysis
        margin_table = Table(title="Margin Analysis", show_header=False)
        margin_table.add_column("Parameter", style="cyan")
        margin_table.add_column("Value", style="green")
        
        margin_table.add_row("Safety Margin (Required)", f"{self.safety_margin:.2f} dB")
        margin_table.add_row("System Operating Margin (SOM)", f"{results['som']:.2f} dB")
        
        # Color-code status
        if results['status'] == "PASS":
            status_color = "green"
        elif results['status'] == "MARGINAL":
            status_color = "yellow"
        else:
            status_color = "red"
        
        margin_table.add_row(
            "Status",
            f"[{status_color}]{results['status']}[/{status_color}] - {results['status_detail']}"
        )
        
        console.print(margin_table)
        console.print()


@click.command()
@click.option('--tx-power', type=float, required=True, help='Transmitter power (dBm)')
@click.option('--rx-sensitivity', type=float, required=True, help='Receiver sensitivity (dBm)')
@click.option('--fiber-length', type=float, required=True, help='Fiber length (km)')
@click.option('--wavelength', type=int, default=1310, help='Wavelength (nm)')
@click.option('--fiber-type', type=click.Choice(['SM', 'MM'], case_sensitive=False), 
              default='SM', help='Fiber type')
@click.option('--connectors', type=int, default=0, help='Number of connectors')
@click.option('--splices', type=int, default=0, help='Number of splices')
@click.option('--safety-margin', type=float, default=3.0, help='Safety margin (dB)')
def main(tx_power, rx_sensitivity, fiber_length, wavelength, fiber_type, 
         connectors, splices, safety_margin):
    """Calculate fiber optic link budget (FOA compliant)."""
    
    budget = LinkBudget(
        tx_power=tx_power,
        rx_sensitivity=rx_sensitivity,
        fiber_length=fiber_length,
        wavelength=wavelength,
        fiber_type=fiber_type,
        connector_count=connectors,
        splice_count=splices,
        safety_margin=safety_margin
    )
    
    budget.print_report()


if __name__ == '__main__':
    main()
