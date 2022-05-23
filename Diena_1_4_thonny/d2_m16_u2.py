platums = float(input("Telpas platums (m)? "))
garums = float(input("Telpas garums (m)? "))
augstums = float(input("Telpas augstums (m)? "))
tilpums = platums*garums*augstums
tilpums = round(tilpums, 2)
print(f"Telpas tilpums ir {tilpums} m³")