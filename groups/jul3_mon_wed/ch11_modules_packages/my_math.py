# I will create a Math class in my_math.py
# it will only have static methods

class Math:
    # add
    # subtract
    # multiply
    # divide
    # power
    PI = 3.141592653589793

    @staticmethod # so called decorator
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        return a / b
    
    # let's make a class method for circle area
    @classmethod # decorator for class method
    def circle_area(cls, r): # note cls instead of self
        return cls.PI * r * r

# i can use static methods without creating an object !!

# if I plan for my module to be used as a script
# good idea is to put main code in this if block

if __name__ == "__main__":
    print("Starting tests")
    print(Math.add(5, 6))
    print(Math.subtract(5, 6))
    print(Math.multiply(5, 6))
    print(Math.divide(5, 6))
    print(Math.circle_area(50))