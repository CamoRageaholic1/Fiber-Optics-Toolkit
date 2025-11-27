# Fiber Toolkit - Core Tools

This directory contains 8 professional fiber optic engineering tools with FOA-compliant calculations.

## 🛠️ Tools

### 1. Link Budget Calculator (`link_budget.py`)
Calculate complete fiber link budgets with FOA-compliant loss values:
- Transmitter power and receiver sensitivity analysis
- Fiber attenuation (wavelength-specific)
- Connector and splice losses
- System Operating Margin (SOM) calculations
- Safety margins (3 dB minimum, 6 dB preferred)

**CLI:** `fiber-link-budget`

### 2. Loss Calculator (`loss_calculator.py`)
Calculate component losses:
- **Connectors:** SC, LC, ST, FC, MPO (UPC/APC polish)
- **Splices:** Fusion (0.1 dB) and Mechanical (0.3 dB)
- **Fiber Attenuation:** SM and MM at various wavelengths
- **Return Loss:** Reflectance calculations

**CLI:** `fiber-loss-calc`

### 3. Wavelength Calculator (`wavelength.py`)
Wavelength-specific analysis:
- Attenuation by wavelength (850nm, 1300nm, 1310nm, 1550nm)
- Chromatic dispersion calculations
- CWDM channel grid (1270-1610nm, 20nm spacing)
- Fiber type recommendations

**CLI:** `fiber-wavelength`

### 4. OTDR Parser (`otdr_parser.py`)
Parse and analyze OTDR trace files:
- Support for Bellcore/Telcordia .sor format
- Event extraction (connectors, splices, breaks)
- Span loss analysis
- Export to JSON/CSV

**CLI:** `fiber-otdr`

### 5. Report Generator (`report_generator.py`)
Generate professional PDF test reports:
- Project information and test details
- Link budget results with pass/fail status
- OTDR analysis summary
- FOA compliance footer

**CLI:** `fiber-report`

### 6. Capacity Planner (`capacity_planner.py`)
Infrastructure design and planning:
- Strand count calculator (with redundancy and growth factors)
- Conduit fill calculations (TIA/EIA standards)
- Splice closure sizing
- Standard fiber counts (6, 12, 24, 48, 72, 144, 288, 432, 576)

**CLI:** `fiber-capacity`

### 7. Standards Reference (`standards_reference.py`)
Quick lookup for industry standards:
- FOA standard loss values
- Fiber type specifications (SM, OM1-OM5)
- Connector types and losses
- TIA/EIA standards list

**CLI:** `fiber-standards`

### 8. CLI Interface (`__main__.py`, `__init__.py`)
Unified command-line interface:
- List all available tools
- Version information
- About the toolkit

## 📚 Standards Compliance

All tools implement:
- **FOA (Fiber Optic Association)** standards
- **TIA-568** commercial building standards
- **TIA-526** optical power loss measurement
- **IEC 61280-4-1** OTDR procedures

## 🚀 Usage

All tools can be used via command-line:

```bash
# Link budget
fiber-link-budget --tx-power 0 --rx-sensitivity -28 --fiber-length 10

# Loss calculation
fiber-loss-calc --calc-type connector --connector-type SC-UPC --count 4

# Wavelength info
fiber-wavelength --wavelength 1550 --info --dispersion

# Standards reference
fiber-standards --show all
```

Or import as Python modules:

```python
from fiber_toolkit.link_budget import LinkBudget
from fiber_toolkit.loss_calculator import LossCalculator
from fiber_toolkit.wavelength import WavelengthCalculator

# Use in your code
budget = LinkBudget(tx_power=0, rx_sensitivity=-28, fiber_length=10)
results = budget.calculate()
```

## 📖 Documentation

See the [main README](../README.md) and [docs/](../docs/) folder for comprehensive documentation.

---

**Built by David Osisek (CFOt, CFOs/s, CFOs/h, CFOs/o)**  
**Author of ["Fiber Optics: A Comprehensive Guide"](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)**
