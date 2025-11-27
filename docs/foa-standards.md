# FOA Standards Reference

This toolkit implements standards from the Fiber Optic Association (FOA).

## Loss Budget Standards

### Connector Loss

| Parameter | Value |
|-----------|-------|
| Typical Loss | 0.75 dB |
| Maximum Loss | 1.0 dB |
| Standard | FOA, TIA-568 |
| Notes | Per mated pair |

### Splice Loss

| Splice Type | Typical | Maximum |
|-------------|---------|----------|
| Fusion | 0.1 dB | 0.3 dB |
| Mechanical | 0.3 dB | 0.5 dB |

### Fiber Attenuation

#### Singlemode (OS2)

| Wavelength | Attenuation |
|------------|-------------|
| 1310nm | 0.35 dB/km |
| 1550nm | 0.25 dB/km |

#### Multimode

| Fiber Type | 850nm | 1300nm |
|------------|-------|--------|
| OM1 (62.5/125) | 3.0 dB/km | 1.0 dB/km |
| OM2-OM5 (50/125) | 3.0 dB/km | 1.0 dB/km |

## Safety Margins

| Margin Type | Value |
|-------------|-------|
| Minimum (FOA) | 3 dB |
| Preferred | 6 dB |

## System Operating Margin (SOM)

```
SOM = Power Budget - Total Loss - Safety Margin
```

**Interpretation:**
- SOM ≥ 6 dB: Excellent
- SOM = 3-6 dB: Good
- SOM = 0-3 dB: Marginal
- SOM < 0 dB: Insufficient (fail)

## TIA/EIA Standards

- TIA-568: Commercial Building Cabling
- TIA-526-14A: Optical Power Loss (Multimode)
- TIA-526-7: Optical Power Loss (Singlemode)
- TIA-598: Fiber Cable Color Coding

## References

- FOA Website: https://www.thefoa.org
- Book: "Fiber Optics: A Comprehensive Guide" by David Osisek
