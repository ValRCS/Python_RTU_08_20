try:
    width=float(input("Ieraksti savas istabas platumu (metros): "))
    height=float(input("Ieraksti savas istabas augstumu (metros): "))
    length=float(input("Ieraksti savas istabas garumu (metros): "))
    capacity=round(width*height*length, 2)
    print(f"Tavas istabas tilpums ir {capacity} m\u00b3.")
except ValueError:
    print("Ievadiet vērtību ciparos! Komata vietā jālieto punkts.")
print("*"*30)