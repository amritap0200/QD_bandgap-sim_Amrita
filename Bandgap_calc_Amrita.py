def qd_bandgap(diameter_nm):
    return 1.8 / (diameter_nm ** 2)
print(f"2nm QD Bandgap: {qd_bandgap(2):.2f} eV")  # Output: 0.45 eV
