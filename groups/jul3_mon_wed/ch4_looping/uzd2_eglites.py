## Cikli 2. uzdevums Eglīte

height = int(input(f"Ievadi eglītes augstumu: "))
 
for n in range(height):
    print(" " * (height - n - 1) + "*" * (2*n + 1))
else:
    print(" " * n + "U")