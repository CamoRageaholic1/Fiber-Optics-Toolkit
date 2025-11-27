"""
Fiber Optics Toolkit
Professional fiber optic engineering tools with FOA-compliant calculations.

Author: David Osisek (CFOt, CFOs/s, CFOs/h, CFOs/o)
Book: https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/

License: MIT
"""

__version__ = '1.0.0'
__author__ = 'David Osisek'

from .link_budget import LinkBudget
from .loss_calculator import LossCalculator
from .wavelength import WavelengthCalculator

__all__ = [
    'LinkBudget',
    'LossCalculator',
    'WavelengthCalculator',
]
