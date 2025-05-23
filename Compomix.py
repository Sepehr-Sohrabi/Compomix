import matplotlib.pyplot as plt

# Modified Halpin-Tsai equation for modulus with random orientation correction
def modified_halpin_tsai_modulus(Ef, Em, Vf, K_o=0.3):
    eta = (Ef / Em - 1) / (Ef / Em + 2)
    Ec = Em * (1 + 2 * eta * Vf) / (1 - eta * Vf)
    Ec_effective = Ec * K_o  # Applying orientation correction factor
    return Ec_effective

# Kelly-Tyson equation for tensile strength
def kelly_tyson_tensile_strength(sigma_f, sigma_m, Vf, Lf, Lc):
    if Lf < Lc:
        sigma_f_eff = sigma_f * (1 - (Lc / Lf))
        if sigma_f_eff < 0:
            sigma_f_eff = 0
    else:
        sigma_f_eff = sigma_f
    sigma_c = sigma_m * (1 - Vf) + Vf * sigma_f_eff
    return sigma_c

def main():
    print("Silk-PGA Composite Property Calculator\n")

    # --- Input range ---
    silk_start = int(input("Enter starting silk fiber percentage (e.g., 20): "))
    silk_end = int(input("Enter ending silk fiber percentage (e.g., 40): "))
    step = int(input("Enter step size (e.g., 5): "))

    if not (0 <= silk_start <= 100 and silk_start < silk_end <= 100):
        print("Error: Invalid range.")
        return

    # --- Fiber Inputs ---
    Lf = float(input("Enter the fiber length (in cm, e.g., 0.5): "))
    d_f_um = float(input("Enter the fiber diameter (in micrometers, e.g., 10): "))
    K_o = float(input("Enter orientation correction factor K_o (e.g., 0.3): "))

    # --- Unit conversion ---
    d_f = d_f_um / 1e4  # convert micrometers to cm

    # --- Material Properties ---
    Ef = 14        # GPa, silk
    Em = 10        # GPa, PGA
    vf = 0.34      # Poisson's ratio, silk
    vm = 0.33      # Poisson's ratio, PGA
    rho_f = 1.35   # g/cm³, silk
    rho_m = 1.45   # g/cm³, PGA

    sigma_f = 500  # MPa, silk
    sigma_m = 85   # MPa, PGA
    tau_m = 65.4   # MPa, assumed matrix shear strength

    # --- Critical Length Calculation (simplified form) ---
    Lc = (sigma_f * d_f) / tau_m
    print(f"\nCalculated Critical Length (Lc) = {Lc:.4f} cm\n")

    # --- Storage ---
    silk_percentages = []
    elastic_moduli = []
    poisson_ratios = []
    densities = []
    tensile_strengths = []

    print("\n%-12s %-20s %-20s %-20s %-20s" % ("Silk (%)", "Elastic Modulus (GPa)", "Poisson's Ratio", "Density (g/cm³)", "Tensile Strength (MPa)"))
    print("-" * 95)

    for percent in range(silk_start, silk_end + 1, step):
        Vf = percent / 100.0
        Vm = 1.0 - Vf

        # Compute composite properties
        Ec = modified_halpin_tsai_modulus(Ef, Em, Vf, K_o)
        nu = Vf * vf + Vm * vm
        rho = Vf * rho_f + Vm * rho_m
        sigma_c = kelly_tyson_tensile_strength(sigma_f, sigma_m, Vf, Lf, Lc)

        # Store values
        silk_percentages.append(percent)
        elastic_moduli.append(Ec)
        poisson_ratios.append(nu)
        densities.append(rho)
        tensile_strengths.append(sigma_c)

        print(f"{percent:<12}{Ec:<20.3f}{nu:<20.3f}{rho:<20.3f}{sigma_c:<20.1f}")

    # --- Plot 1: Elastic Modulus, Poisson's Ratio, Density ---
    plt.figure(figsize=(10, 6))
    plt.plot(silk_percentages, elastic_moduli, marker='o', label="Elastic Modulus (GPa)")
    plt.plot(silk_percentages, poisson_ratios, marker='s', label="Poisson's Ratio")
    plt.plot(silk_percentages, densities, marker='^', label="Density (g/cm³)")
    plt.title("PGA-Silk Composite Properties vs. Silk Content")
    plt.xlabel("Silk Fiber Content (%)")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- Plot 2: Tensile Strength Only ---
    plt.figure(figsize=(8, 5))
    plt.plot(silk_percentages, tensile_strengths, color='darkred', marker='x', linewidth=2, label="Tensile Strength (MPa)")
    plt.title("Tensile Strength vs. Silk Content")
    plt.xlabel("Silk Fiber Content (%)")
    plt.ylabel("Tensile Strength (MPa)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
