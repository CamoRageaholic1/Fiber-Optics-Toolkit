#!/usr/bin/env python3
"""
Loss Calculator
Calculate connector, splice, and fiber losses.

Author: David Osisek (CFOt)
"""

import click
from rich.console import Console
from rich.table import Table
from typing import Dict

class LossCalculator:
    """Calculate various fiber optic losses."""
    
    CONNECTOR_TYPES = {
        'SC-UPC': 0.25,
        'SC-APC': 0.30,
        'LC-UPC': 0.25,
        'LC-APC': 0.30,
        'ST': 0.50,
        'FC-UPC': 0.30,
        'FC-APC': 0.35,
        'MPO': 0.50,
    }
    
    SPLICE_TYPES = {
        'fusion': 0.1,
        'mechanical': 0.3,
    }
    
    FIBER_ATTENUATION = {
        'SM': {1310: 0.35, 1550: 0.25},
        'MM-OM1': {850: 3.0, 1300: 1.0},
        'MM-OM2': {850: 3.0, 1300: 1.0},
        'MM-OM3': {850: 3.0, 1300: 1.0},
        'MM-OM4': {850: 3.0, 1300: 1.0},
        'MM-OM5': {850: 3.0, 1300: 1.0},
    }

    @classmethod
    def connector_loss(cls, connector_type: str, count: int = 1) -> Dict:
        """Calculate connector loss."""
        loss_per = cls.CONNECTOR_TYPES.get(connector_type.upper(), 0.75)
        total = loss_per * count
        return {
            'connector_type': connector_type,
            'count': count,
            'loss_per_connector': loss_per,
            'total_loss': total
        }

    @classmethod  
    def splice_loss(cls, splice_type: str, count: int = 1) -> Dict:
        """Calculate splice loss."""
        loss_per = cls.SPLICE_TYPES.get(splice_type.lower(), 0.1)
        total = loss_per * count
        return {
            'splice_type': splice_type,
            'count': count,
            'loss_per_splice': loss_per,
            'total_loss': total
        }

    @classmethod
    def fiber_attenuation(cls, fiber_type: str, wavelength: int, length: float) -> Dict:
        """Calculate fiber attenuation."""
        atten_map = cls.FIBER_ATTENUATION.get(fiber_type, cls.FIBER_ATTENUATION['SM'])
        closest_wl = min(atten_map.keys(), key=lambda x: abs(x - wavelength))
        atten_per_km = atten_map[closest_wl]
        total = atten_per_km * length
        return {
            'fiber_type': fiber_type,
            'wavelength': wavelength,
            'length_km': length,
            'attenuation_per_km': atten_per_km,
            'total_loss': total
        }

@click.command()
@click.option('--calc-type', type=click.Choice(['connector', 'splice', 'fiber']), required=True)
@click.option('--connector-type', type=str, help='Connector type (SC-UPC, LC-APC, etc.)')
@click.option('--splice-type', type=click.Choice(['fusion', 'mechanical']), help='Splice type')
@click.option('--fiber-type', type=str, help='Fiber type (SM, MM-OM3, etc.)')
@click.option('--wavelength', type=int, help='Wavelength (nm)')
@click.option('--length', type=float, help='Fiber length (km)')
@click.option('--count', type=int, default=1, help='Number of connectors/splices')
def main(calc_type, connector_type, splice_type, fiber_type, wavelength, length, count):
    """Calculate fiber optic component losses."""
    console = Console()
    
    if calc_type == 'connector':
        result = LossCalculator.connector_loss(connector_type, count)
        console.print(f"\nConnector Loss: {result['total_loss']:.2f} dB")
    elif calc_type == 'splice':
        result = LossCalculator.splice_loss(splice_type, count)
        console.print(f"\nSplice Loss: {result['total_loss']:.2f} dB")
    elif calc_type == 'fiber':
        result = LossCalculator.fiber_attenuation(fiber_type, wavelength, length)
        console.print(f"\nFiber Loss: {result['total_loss']:.2f} dB")

if __name__ == '__main__':
    main()
