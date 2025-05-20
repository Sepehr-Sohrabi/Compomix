# Compomix

**Compomix** is a Python tool that calculates and visualizes the mechanical properties of fiber-reinforced composites using the modified Halpin-Tsai and Kelly-Tyson models. It's designed with silk-PGA biocomposites in mind but can be easily adapted for other fiber/matrix combinations.

## Features
- Estimates effective elastic modulus with random orientation correction.
- Computes tensile strength using Kelly-Tyson equation.
- Includes critical length estimation.
- Outputs Poisson’s ratio and density.
- Generates two clean plots for analysis.

## How it works
1. Input Parameters
- You will be prompted to enter:
  -Start and end silk fiber volume fractions (%)
  -Step size
  -Fiber length (cm)
  -Fiber diameter (μm)
  -Orientation correction factor K_o (e.g., 0.3 for randomly oriented short fibers)

2. Outputs
- You'll get:
  -Terminal table with modulus, strength, density, and Poisson’s ratio
  -Two interactive plots for visual analysis

## Customization
If you want to use it for other materials, just replace the values under # --- Material Properties --- in compomix.py.

## Dependencies
1. Python 3.x
2. matplotlib

## License
This code is completely open-source. Use it. Modify it. Abuse it. No credit required :)

## Citation
If you use **Compomix** in your work, please cite it using the metadata in the [`CITATION.cff`](./CITATION.cff) file, or use the following format:
Sohrabi, Sepehr. Compomix: A Micromechanical Composite Property Calculator (v1.0.0), 2025. GitHub repository: https://github.com/Sepehr-Sohrabi/Compomix

Author
Sepehr Sohrabi – MSc student in Biomechanical Engineering.

## How to Use
1. Clone the repo
```bash
git clone https://github.com/sepehr-sohrabi/Compomix.git
cd Compomix
