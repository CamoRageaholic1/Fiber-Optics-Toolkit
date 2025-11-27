#!/usr/bin/env python3
"""
Wavelength Calculator
Wavelength-specific attenuation, dispersion, and CWDM channels.

Author: David Osisek (CFOt)
"""

import click
from rich.console import Console
from rich.table import Table

class WavelengthCalculator:
    """Wavelength-specific calculations."""
    
    WAVELENGTHS = {
        850: {'window': 'First', 'fiber': 'MM', 'disp': 0, 'atten_mm': 3.0},
        1300: {'window': 'Second', 'fiber': 'MM/SM', 'disp': 0, 'atten_mm': 1.0, 'atten_sm': 0.35},
        1310: {'window': 'O-band', 'fiber': 'SM', 'disp': 0, 'atten_sm': 0.35},
        1550: {'window': 'C-band', 'fiber': 'SM', 'disp': 17, 'atten_sm': 0.25},
    }
    
    @classmethod
    def get_wavelength_info(cls, wavelength: int):
        """Get wavelength information."""
        return cls.WAVELENGTHS.get(wavelength, {})
    
    @classmethod
    def calculate_dispersion(cls, wavelength: int, length: float) -> float:
        """Calculate chromatic dispersion."""
        info = cls.get_wavelength_info(wavelength)
        disp_coeff = info.get('disp', 17)
        return disp_coeff * length
    
    @classmethod
    def list_cwdm_channels(cls):
        """List CWDM wavelength channels."""
        channels = []
        for i, wl in enumerate(range(1270, 1620, 20), 1):
            channels.append({'channel': i, 'wavelength': wl})
        return channels

@click.command()
@click.option('--wavelength', type=int, help='Wavelength (nm)')
@click.option('--info', is_flag=True, help='Show wavelength info')
@click.option('--dispersion', is_flag=True, help='Calculate dispersion')
@click.option('--length', type=float, help='Fiber length (km) for dispersion')
@click.option('--list-cwdm', is_flag=True, help='List CWDM channels')
def main(wavelength, info, dispersion, length, list_cwdm):
    """Wavelength calculator and CWDM channel reference."""
    console = Console()
    
    if list_cwdm:
        channels = WavelengthCalculator.list_cwdm_channels()
        console.print("\n[bold cyan]CWDM Channels[/bold cyan]")
        for ch in channels:
            console.print(f"Ch {ch['channel']:2d}: {ch['wavelength']} nm")
        return
    
    if info and wavelength:
        wl_info = WavelengthCalculator.get_wavelength_info(wavelength)
        console.print(f"\nWavelength: {wavelength} nm")
        console.print(f"Window: {wl_info.get('window', 'N/A')}")
        console.print(f"Fiber: {wl_info.get('fiber', 'N/A')}")
    
    if dispersion and wavelength and length:
        disp = WavelengthCalculator.calculate_dispersion(wavelength, length)
        console.print(f"\nDispersion: {disp:.2f} ps/(nm·km)")

if __name__ == '__main__':
    main()
