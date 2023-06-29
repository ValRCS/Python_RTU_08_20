# modules in packages should have short all lowercase names
# they should organize code into logical units - by theme or functionality

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None # could raise exception
    return a / b