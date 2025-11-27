# Quick Start Guide

## Installation

```bash
# Clone repository
git clone https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit.git
cd Fiber-Optics-Toolkit

# Install dependencies
pip install -r requirements.txt

# Or install as package
pip install -e .
```

## Basic Usage

### Link Budget Calculator

```bash
fiber-link-budget \
  --tx-power 0 \
  --rx-sensitivity -28 \
  --fiber-length 10 \
  --wavelength 1310 \
  --connectors 4 \
  --splices 2
```

### Loss Calculator

```bash
# Connector loss
fiber-loss-calc --calc-type connector --connector-type SC-UPC --count 4

# Fiber attenuation
fiber-loss-calc --calc-type fiber --fiber-type SM --wavelength 1550 --length 25.5
```

### Wavelength Information

```bash
fiber-wavelength --wavelength 1550 --info --dispersion --length 50
```

### Standards Reference

```bash
fiber-standards --show all
```

### Capacity Planning

```bash
fiber-capacity --calc-type strands --endpoints 24
```

## Tips

- Use `--help` on any command for detailed options
- All calculations follow FOA standards
- Safety margins default to 3 dB (FOA minimum)
- Connector loss defaults to 0.75 dB (FOA typical)
