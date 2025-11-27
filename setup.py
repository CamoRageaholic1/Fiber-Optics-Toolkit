#!/usr/bin/env python3
"""
Fiber Optics Toolkit
Professional fiber optic engineering tools with FOA-compliant calculations.

Author: David Osisek (CFOt, CFOs/s, CFOs/h, CFOs/o)
Book: Fiber Optics: A Comprehensive Guide (Amazon)
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='fiber-optics-toolkit',
    version='1.0.0',
    description='Professional fiber optic engineering toolkit with FOA-compliant calculators',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit',
    author='David Osisek',
    author_email='david.osisek@example.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='fiber optics, FOA, telecommunications, network engineering, OTDR, link budget',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.24.0',
        'pandas>=2.0.0',
        'click>=8.1.0',
        'rich>=13.0.0',
        'tabulate>=0.9.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.0',
        'reportlab>=4.0.0',
        'Pillow>=10.0.0',
        'openpyxl>=3.1.0',
        'xlsxwriter>=3.1.0',
    ],
    entry_points={
        'console_scripts': [
            'fiber-link-budget=fiber_toolkit.link_budget:main',
            'fiber-loss-calc=fiber_toolkit.loss_calculator:main',
            'fiber-wavelength=fiber_toolkit.wavelength:main',
            'fiber-otdr=fiber_toolkit.otdr_parser:main',
            'fiber-report=fiber_toolkit.report_generator:main',
            'fiber-capacity=fiber_toolkit.capacity_planner:main',
            'fiber-standards=fiber_toolkit.standards_reference:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit/issues',
        'Source': 'https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit',
        'Author Book': 'https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/',
    },
)
