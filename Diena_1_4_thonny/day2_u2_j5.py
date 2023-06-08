platums = input("Kādā platumā ir telpa? ")
garums = input("Kāds garums ir telpai? ")
augstums = input("Kāds ir griestu augstums? ")
a=float(platums)
b=float(garums)
c=float(augstums)
tilpums = a * b * c
print(f"Telpas tilpums sastāda {tilpums:.2f} m³.")