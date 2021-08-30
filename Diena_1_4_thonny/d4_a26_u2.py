height = 5

for i in range(height,-1, -1):
    print(' ' * (height - i) + '*' * (2*i + 1))
    
print(list(range(height)))    
print(list(range(height,-1, -1)))