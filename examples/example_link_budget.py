#!/usr/bin/env python3
"""
Example: Link Budget Calculation

Demonstrates how to use the LinkBudget class.
"""

from fiber_toolkit.link_budget import LinkBudget

def example_basic_link():
    """Example 1: Basic 10km singlemode link."""
    print("\n" + "="*70)
    print("Example 1: Basic 10km Singlemode Link")
    print("="*70)
    
    budget = LinkBudget(
        tx_power=0.0,
        rx_sensitivity=-28.0,
        fiber_length=10.0,
        wavelength=1310,
        fiber_type='SM',
        connector_count=4,
        splice_count=2,
    )
    
    budget.print_report()

def example_long_haul():
    """Example 2: Long-haul 50km link."""
    print("\n" + "="*70)
    print("Example 2: Long-Haul 50km Link")
    print("="*70)
    
    budget = LinkBudget(
        tx_power=3.0,
        rx_sensitivity=-32.0,
        fiber_length=50.0,
        wavelength=1550,
        fiber_type='SM',
        connector_count=6,
        splice_count=10,
        safety_margin=6.0,
    )
    
    budget.print_report()

def example_programmatic():
    """Example 3: Access results programmatically."""
    print("\n" + "="*70)
    print("Example 3: Programmatic Access")
    print("="*70)
    
    budget = LinkBudget(
        tx_power=0.0,
        rx_sensitivity=-28.0,
        fiber_length=10.0,
        wavelength=1310,
        fiber_type='SM',
        connector_count=4,
        splice_count=2,
    )
    
    results = budget.calculate()
    
    print(f"\nPower Budget: {results['power_budget']:.2f} dB")
    print(f"Total Loss: {results['total_loss']:.2f} dB")
    print(f"SOM: {results['som']:.2f} dB")
    print(f"Status: {results['status']} - {results['status_detail']}")
    
    if results['som'] < 3.0:
        print("\n⚠ WARNING: Insufficient margin!")

if __name__ == '__main__':
    example_basic_link()
    example_long_haul()
    example_programmatic()
    
    print("\n" + "="*70)
    print("Examples Complete!")
    print("="*70 + "\n")
