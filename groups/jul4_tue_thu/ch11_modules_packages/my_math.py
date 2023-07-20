# I will have a Math class for my math operations
# I will be using class and static methods

class Math:
    PI = 3.14159265 # class variable
    @staticmethod # decorator - means we do not need to pass self
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    # i can also have a class method
    # i need to acces class variable PI but I do not need any object variables
    @classmethod
    def circle_area(cls, r):
        return cls.PI * r * r
    
# lets add main guard
if __name__ == "__main__":
    print("This is the my_math module run directly")
    # let's test some functions
    print(Math.add(2, 3)) # notice I did not make any objects!!
    print(Math.sub(2, 3))
    print(Math.circle_area(10))
    # let's check if we can access x's name
    assert Math.add(2, 3) == 5 # simple sanity check
    assert Math.sub(2, 3) == -1 # simple sanity check
    assert Math.circle_area(10) == 314.159265 # simple sanity check