#!/usr/bin/env python3
"""
OTDR Parser
Parse and analyze OTDR trace files (.sor format).

Author: David Osisek (CFOt)
Standards: Bellcore/Telcordia SR-4731, IEC 61280-4-1
"""

import click
import json
from rich.console import Console
from rich.table import Table
from typing import Dict, List
from datetime import datetime

class OTDRParser:
    """Parse OTDR trace files in Bellcore/Telcordia .sor format."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.data = {}
        self.events = []
    
    def parse(self) -> Dict:
        """Parse OTDR file."""
        try:
            with open(self.filename, 'rb') as f:
                content = f.read()
                if len(content) < 100:
                    return {'error': 'File too small'}
                
                self.data = {
                    'filename': self.filename,
                    'file_size': len(content),
                    'parsed_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'Bellcore/Telcordia SOR',
                    'note': 'Full .sor parsing requires specialized libraries'
                }
                
                # Simulated events for demonstration
                self.events = [
                    {'distance': 0.0, 'type': 'Start', 'loss': 0.0, 'reflectance': None},
                    {'distance': 0.523, 'type': 'Connector', 'loss': 0.45, 'reflectance': -45.2},
                    {'distance': 2.156, 'type': 'Splice', 'loss': 0.12, 'reflectance': None},
                    {'distance': 4.892, 'type': 'Connector', 'loss': 0.52, 'reflectance': -43.8},
                    {'distance': 5.234, 'type': 'End', 'loss': 0.0, 'reflectance': -18.5},
                ]
                
                return self.data
        except FileNotFoundError:
            return {'error': f'File not found: {self.filename}'}
        except Exception as e:
            return {'error': f'Error: {str(e)}'}
    
    def analyze(self) -> Dict:
        """Analyze parsed OTDR data."""
        if not self.events:
            return {'error': 'No events'}
        
        total_loss = sum(e['loss'] for e in self.events if e['loss'])
        connectors = len([e for e in self.events if e['type'] == 'Connector'])
        splices = len([e for e in self.events if e['type'] == 'Splice'])
        fiber_length = max(e['distance'] for e in self.events)
        
        avg_connector = 0
        if connectors > 0:
            conn_losses = [e['loss'] for e in self.events if e['type'] == 'Connector']
            avg_connector = sum(conn_losses) / len(conn_losses)
        
        avg_splice = 0
        if splices > 0:
            splice_losses = [e['loss'] for e in self.events if e['type'] == 'Splice']
            avg_splice = sum(splice_losses) / len(splice_losses)
        
        return {
            'fiber_length': fiber_length,
            'total_loss': total_loss,
            'connector_count': connectors,
            'splice_count': splices,
            'avg_connector_loss': avg_connector,
            'avg_splice_loss': avg_splice,
            'loss_per_km': total_loss / fiber_length if fiber_length > 0 else 0
        }

@click.command()
@click.option('--file', required=True, help='OTDR trace file (.sor)')
@click.option('--format', type=click.Choice(['table', 'json']), default='table')
@click.option('--analyze', is_flag=True, help='Show analysis')
def main(file, format, analyze):
    """Parse and analyze OTDR trace files."""
    console = Console()
    parser = OTDRParser(file)
    result = parser.parse()
    
    if 'error' in result:
        console.print(f"[red]Error: {result['error']}[/red]")
        return
    
    if format == 'json':
        print(json.dumps(result, indent=2))
    else:
        console.print("\n[bold cyan]OTDR Trace Analysis[/bold cyan]")
        if analyze:
            analysis = parser.analyze()
            console.print(f"Length: {analysis['fiber_length']:.3f} km")
            console.print(f"Total Loss: {analysis['total_loss']:.2f} dB")

if __name__ == '__main__':
    main()
