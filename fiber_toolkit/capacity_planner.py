#!/usr/bin/env python3
"""
Capacity Planner
Fiber strand count, conduit fill, and splice closure sizing.

Author: David Osisek (CFOt)
"""

import click
import math
from rich.console import Console
from rich.table import Table

class CapacityPlanner:
    """Infrastructure capacity planning."""
    
    STANDARD_COUNTS = [6, 12, 24, 48, 72, 144, 288, 432, 576]
    
    @classmethod
    def calculate_strand_count(cls, endpoints: int, redundancy: float = 1.5, 
                               future_growth: float = 1.3):
        """Calculate required strand count."""
        base = endpoints * 2  # Assume duplex
        with_redundancy = base * redundancy
        with_growth = with_redundancy * future_growth
        recommended = min([c for c in cls.STANDARD_COUNTS if c >= with_growth], 
                         default=cls.STANDARD_COUNTS[-1])
        return {
            'base_strands': base,
            'with_redundancy': with_redundancy,
            'with_growth': with_growth,
            'recommended_count': recommended
        }
    
    @classmethod
    def conduit_fill(cls, conduit_diameter: float, cable_diameter: float,
                     cable_count: int = 1):
        """Calculate conduit fill percentage."""
        conduit_area = math.pi * (conduit_diameter / 2) ** 2
        cable_area = math.pi * (cable_diameter / 2) ** 2
        total_cable_area = cable_area * cable_count
        fill_percent = (total_cable_area / conduit_area) * 100
        
        # TIA standards: 1 cable=53%, 2=31%, 3+=40%
        if cable_count == 1:
            max_fill = 53
        elif cable_count == 2:
            max_fill = 31
        else:
            max_fill = 40
        
        return {
            'conduit_area': conduit_area,
            'cable_area_total': total_cable_area,
            'fill_percent': fill_percent,
            'max_fill_percent': max_fill,
            'compliant': fill_percent <= max_fill
        }

@click.command()
@click.option('--calc-type', type=click.Choice(['strands', 'conduit']), required=True)
@click.option('--endpoints', type=int, help='Number of endpoints')
@click.option('--redundancy', type=float, default=1.5, help='Redundancy factor')
@click.option('--growth', type=float, default=1.3, help='Growth factor')
@click.option('--conduit-diameter', type=float, help='Conduit diameter (mm)')
@click.option('--cable-diameter', type=float, help='Cable diameter (mm)')
@click.option('--cable-count', type=int, default=1, help='Number of cables')
def main(calc_type, endpoints, redundancy, growth, conduit_diameter, cable_diameter, cable_count):
    """Capacity planning for fiber infrastructure."""
    console = Console()
    
    if calc_type == 'strands':
        result = CapacityPlanner.calculate_strand_count(endpoints, redundancy, growth)
        console.print(f"\nRecommended strand count: {result['recommended_count']}")
    elif calc_type == 'conduit':
        result = CapacityPlanner.conduit_fill(conduit_diameter, cable_diameter, cable_count)
        console.print(f"\nFill: {result['fill_percent']:.1f}% (Max: {result['max_fill_percent']}%)")
        console.print(f"Compliant: {'Yes' if result['compliant'] else 'No'}")

if __name__ == '__main__':
    main()
