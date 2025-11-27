#!/usr/bin/env python3
"""
Fiber Optics Toolkit - Main CLI Entry Point

Author: David Osisek (CFOt)
"""

import click
from rich.console import Console
from rich.table import Table

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """
    Fiber Optics Toolkit - Professional FOA-compliant tools.
    
    Built by David Osisek (CFOt, CFOs/s, CFOs/h, CFOs/o)
    Author of "Fiber Optics: A Comprehensive Guide" (Amazon)
    """
    pass

@cli.command()
def tools():
    """List all available tools."""
    console = Console()
    
    console.print("\n[bold cyan]Fiber Optics Toolkit - Available Tools[/bold cyan]")
    console.print("="*70)
    
    table = Table(show_header=True)
    table.add_column("Tool", style="cyan")
    table.add_column("Command", style="green")
    table.add_column("Description", style="yellow")
    
    tools_list = [
        ("Link Budget Calculator", "fiber-link-budget", "Calculate fiber link budgets (FOA)"),
        ("Loss Calculator", "fiber-loss-calc", "Calculate component losses"),
        ("Wavelength Calculator", "fiber-wavelength", "Wavelength-specific calculations"),
        ("OTDR Parser", "fiber-otdr", "Parse and analyze OTDR traces"),
        ("Report Generator", "fiber-report", "Generate PDF test reports"),
        ("Capacity Planner", "fiber-capacity", "Plan fiber infrastructure"),
        ("Standards Reference", "fiber-standards", "Quick reference for FOA/TIA standards"),
    ]
    
    for tool, command, desc in tools_list:
        table.add_row(tool, command, desc)
    
    console.print(table)
    console.print("\n[dim]Run any command with --help for detailed usage[/dim]\n")

@cli.command()
def about():
    """About the Fiber Optics Toolkit."""
    console = Console()
    
    console.print("\n[bold cyan]Fiber Optics Toolkit v1.0.0[/bold cyan]")
    console.print("\nProfessional fiber optic engineering tools with FOA-compliant calculations.")
    console.print("\n[bold]Author:[/bold] David Osisek")
    console.print("[bold]Certifications:[/bold] CFOt, CFOs/s, CFOs/h, CFOs/o")
    console.print("[bold]Published Book:[/bold] \"Fiber Optics: A Comprehensive Guide\" (Amazon)")
    console.print("\n[bold]Standards Compliance:[/bold]")
    console.print("• Fiber Optic Association (FOA)")
    console.print("• TIA/EIA-568 Commercial Building Standards")
    console.print("• IEC 61280-4-1 OTDR Procedures")
    console.print("\n[bold]GitHub:[/bold] github.com/CamoRageaholic1/Fiber-Optics-Toolkit")
    console.print("[bold]License:[/bold] MIT\n")

if __name__ == '__main__':
    cli()
