import random
random.seed(42)
# so random numbers are really pseudo-random so with specific seed number they are consistent
numbers = [random.randint(1,6) for n in range(100)]
floats = [random.random() for _ in range(10)] 
# if I do not use the inner variable convention is to use _
print(max(numbers))
print(numbers[:5], floats[:5])