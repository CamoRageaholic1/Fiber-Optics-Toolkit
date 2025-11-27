# Fiber Optics Toolkit 🔬

[![Author - Published Writer](https://img.shields.io/badge/Author-Published_Writer-blue)](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FOA Compliant](https://img.shields.io/badge/FOA-Compliant-green.svg)](https://www.thefoa.org/)

Professional fiber optic engineering toolkit with 8 FOA-compliant calculators and tools for link budgets, OTDR analysis, loss calculations, and infrastructure planning.

**Author:** David Osisek (CFOt, CFOs/s, CFOs/h, CFOs/o) | [Published Book on Amazon](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)

---

## 📚 Learn More About Fiber Optics

> **Check out the author's book: ["Fiber Optics: A Comprehensive Guide"](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)** 
> This toolkit was built as a practical companion to the book, implementing all FOA standards and calculations in professional-grade Python tools.

---

## 🎯 Overview

This toolkit provides 8 professional-grade tools for fiber optic engineering, all compliant with FOA (Fiber Optic Association), TIA-568, and IEC standards. Built by a CFOt-certified fiber professional with 15+ years of field experience.

### ✨ Features

- 🔍 **FOA-Compliant Calculations** - All tools follow industry standards
- 📊 **Professional CLI Interface** - Beautiful terminal output with Rich
- 📈 **Link Budget Analysis** - Calculate system operating margins
- 🔌 **Loss Calculations** - Connectors, splices, fiber attenuation
- 🌈 **Wavelength Tools** - Dispersion, attenuation, CWDM channels
- 📉 **OTDR Parser** - Parse and analyze .sor trace files
- 📄 **PDF Reports** - Generate professional test reports
- 🏗️ **Capacity Planning** - Infrastructure design tools
- 📖 **Standards Reference** - Quick lookup for FOA/TIA/IEC standards

---

## 🛠️ Tools Included

### 1. Link Budget Calculator
Calculate complete fiber link budgets with FOA-compliant loss values:
- Transmitter power and receiver sensitivity
- Fiber attenuation (wavelength-specific)
- Connector and splice losses
- Safety margins (3 dB minimum, 6 dB preferred)
- System Operating Margin (SOM) analysis

### 2. Loss Calculator
Calculate component losses:
- **Connectors**: SC, LC, ST, FC, MPO (UPC/APC polish)
- **Splices**: Fusion (0.1 dB typical) and Mechanical (0.3 dB typical)
- **Fiber Attenuation**: SM and MM at various wavelengths
- **Return Loss**: Reflectance calculations

### 3. Wavelength Calculator
Wavelength-specific information and calculations:
- Attenuation by wavelength (850nm, 1300nm, 1310nm, 1550nm)
- Chromatic dispersion calculations
- CWDM channel grid (1270-1610nm)
- Fiber type recommendations

### 4. OTDR Parser
Parse and analyze OTDR trace files:
- Support for Bellcore/Telcordia .sor format
- Event extraction (connectors, splices, breaks)
- Span loss analysis
- Export to JSON/CSV

### 5. Report Generator
Generate professional PDF test reports:
- Project information and test details
- Link budget results with pass/fail status
- OTDR analysis summary
- FOA compliance footer
- Professional formatting

### 6. Capacity Planner
Infrastructure design and planning:
- Strand count calculator (with redundancy and growth)
- Conduit fill calculations (TIA/EIA standards)
- Splice closure sizing
- Standard fiber counts (6, 12, 24, 48, 72, 144, 288, 432, 576)

### 7. Standards Reference
Quick lookup for industry standards:
- FOA standard loss values
- Fiber type specifications (SM, OM1-OM5)
- Connector types and losses
- TIA/EIA standards list

### 8. CLI Interface
Unified command-line interface:
- Easy-to-use commands for all tools
- Rich formatted output with color
- Comprehensive help documentation
- Pip-installable package

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit.git
cd Fiber-Optics-Toolkit

# Install dependencies
pip install -r requirements.txt

# Or install as package
pip install -e .
```

---

## 🚀 Quick Start

### Link Budget Calculation
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
# Calculate connector loss
fiber-loss-calc --calc-type connector --connector-type SC-UPC --count 4

# Calculate fiber attenuation
fiber-loss-calc --calc-type fiber --fiber-type SM --wavelength 1550 --length 25.5
```

### Wavelength Information
```bash
# Get wavelength details
fiber-wavelength --wavelength 1550 --info --dispersion --attenuation

# List CWDM channels
fiber-wavelength --list-cwdm
```

### Standards Reference
```bash
# Show all standards
fiber-standards --show all

# Show FOA standards only
fiber-standards --show foa
```

### Capacity Planning
```bash
# Calculate strand count
fiber-capacity --calc-type strands --endpoints 24 --redundancy 1.5 --growth 1.3

# Check conduit fill
fiber-capacity --calc-type conduit --conduit-diameter 25 --cable-diameter 14
```

---

## 📚 Documentation

- **[Quick Start Guide](docs/quick-start.md)** - Get up and running quickly
- **[FOA Standards](docs/foa-standards.md)** - Detailed standards reference
- **[Examples](examples/)** - Python code examples
- **[Contributing](CONTRIBUTING.md)** - How to contribute

---

## 🎓 Standards Compliance

This toolkit implements the following industry standards:

- **FOA (Fiber Optic Association)** - Standard loss values and test procedures
- **TIA-568** - Commercial Building Cabling Standard
- **TIA-526-14A** - Optical Power Loss Measurements (Multimode)
- **TIA-526-7** - Optical Power Loss Measurements (Singlemode)
- **TIA-598** - Optical Fiber Cable Color Coding
- **IEC 61280-4-1** - OTDR Measurement Procedures

---

## 👨‍💻 About the Author

**David Osisek** is a CFOt-certified fiber optic professional with multiple FOA certifications (CFOt, CFOs/s, CFOs/h, CFOs/o) and over 15 years of field experience in fiber optics installation, testing, and troubleshooting.

### Published Work
**["Fiber Optics: A Comprehensive Guide"](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)** - Available on Amazon

This toolkit serves as a practical companion to the book, providing professional-grade tools that implement the standards and calculations covered in the text.

### Certifications
- **CFOt** - Certified Fiber Optic Technician
- **CFOs/s** - Certified Fiber Optic Specialist (Singlemode)
- **CFOs/h** - Certified Fiber Optic Specialist (Hands-on)
- **CFOs/o** - Certified Fiber Optic Specialist (Outside Plant)
- **Bachelor's Degree** - Software Development
- **Master's Degree** - IT Security

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

All contributions must:
- Follow FOA/TIA standards
- Include documentation
- Pass code quality checks
- Include examples where appropriate

---

## 📖 Recommended Reading

1. **["Fiber Optics: A Comprehensive Guide" by David Osisek](https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/)** - The companion book to this toolkit
2. **FOA Reference Guide** - Free online resource from FOA
3. **TIA-568 Standards** - Commercial building cabling
4. **The Fiber Optic Association** - https://www.thefoa.org/

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🔗 Links

- **GitHub Repository**: https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit
- **Author's Book**: https://www.amazon.com/Fiber-Optics-Comprehensive-David-Osisek/dp/B0C91JYN7K/
- **Issues**: https://github.com/CamoRageaholic1/Fiber-Optics-Toolkit/issues
- **FOA Website**: https://www.thefoa.org/

---

## 💡 Use Cases

- **Pre-installation planning** - Calculate link budgets before deployment
- **Post-installation testing** - Analyze OTDR results and generate reports
- **Troubleshooting** - Identify excessive losses and failure points
- **Capacity planning** - Design infrastructure for growth
- **Education** - Learn FOA standards and calculations
- **Professional documentation** - Generate compliant test reports

---

**Built by a published author and CFOt-certified professional for real-world fiber optic deployments** 🔬
