#!/usr/bin/env python3
"""
Standards Reference
Quick reference for FOA, TIA, IEC standards.

Author: David Osisek (CFOt)
"""

import click
from rich.console import Console
from rich.table import Table

class StandardsReference:
    """Quick reference for fiber optic standards."""
    
    FOA_STANDARDS = {
        'connector_loss': {'typical': '0.75 dB', 'maximum': '1.0 dB'},
        'fusion_splice': {'typical': '0.1 dB', 'maximum': '0.3 dB'},
        'mechanical_splice': {'typical': '0.3 dB', 'maximum': '0.5 dB'},
        'safety_margin': {'minimum': '3 dB', 'preferred': '6 dB'},
    }
    
    FIBER_TYPES = {
        'SM (OS2)': {'core': '9 μm', 'wavelengths': '1310nm, 1550nm', 
                     'atten_1310': '0.35 dB/km', 'atten_1550': '0.25 dB/km'},
        'MM OM3': {'core': '50 μm', 'wavelengths': '850nm', 
                   'atten_850': '3.0 dB/km', 'bandwidth': '2000 MHz·km'},
        'MM OM4': {'core': '50 μm', 'wavelengths': '850nm',
                   'atten_850': '3.0 dB/km', 'bandwidth': '4700 MHz·km'},
    }
    
    @classmethod
    def show_foa_standards(cls):
        """Display FOA standards."""
        console = Console()
        console.print("\n[bold cyan]FOA Standard Loss Values[/bold cyan]")
        for component, values in cls.FOA_STANDARDS.items():
            console.print(f"\n{component.replace('_', ' ').title()}:")
            for key, val in values.items():
                console.print(f"  {key.title()}: {val}")
    
    @classmethod
    def show_fiber_types(cls):
        """Display fiber types."""
        console = Console()
        console.print("\n[bold cyan]Fiber Type Specifications[/bold cyan]")
        for fiber, specs in cls.FIBER_TYPES.items():
            console.print(f"\n{fiber}:")
            for key, val in specs.items():
                console.print(f"  {key.replace('_', ' ').title()}: {val}")

@click.command()
@click.option('--show', type=click.Choice(['foa', 'fibers', 'all']), default='all')
def main(show):
    """Fiber optics standards quick reference."""
    if show in ['foa', 'all']:
        StandardsReference.show_foa_standards()
    if show in ['fibers', 'all']:
        StandardsReference.show_fiber_types()

if __name__ == '__main__':
    main()
