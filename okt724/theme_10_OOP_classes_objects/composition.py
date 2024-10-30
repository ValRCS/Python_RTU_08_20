# we've learned about inheritance, now let's learn about composition
# in real life inheritance is not always the best solution
# more often composition is better
# the idea is that one class has another class as a property

# let's look at Car that has Engine and Wheels as properties

class Engine:
    def __init__(self, power=100):
        self.power = power
        self.is_on = False
        print(f"Engine created with power {self.power} hp")

    # let's have engine turn on
    def turn_on(self):
        self.is_on = True
        print("Engine started")

    # let's have engine turn off
    def turn_off(self):
        self.is_on = False
        print("Engine stopped")

class Wheel:
    def __init__(self, diameter=16):
        self.diameter = diameter
        self.is_rotating = False
        print(f"Wheel created with diameter {self.diameter} inches")

    # let's have wheel turn
    def turn(self):
        self.is_rotating = True
        print("Wheel turning")

    # let's have wheel stop
    def stop(self):
        self.is_rotating = False
        print("Wheel stopped")

class Car:
    def __init__(self, make="VW", model="Golf", year=2000, engine=None, wheels=None):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.wheels = wheels
        print(f"Car created: {self.make} {self.model} {self.year}")

    def start(self):
        if self.engine is not None:
            self.engine.turn_on()
        if self.wheels is not None:
            # here we assume that we have a sequence of wheels (list, tuple, set, etc.)
            for wheel in self.wheels:
                wheel.turn()

    def stop(self):
        if self.engine is not None:
            self.engine.turn_off()
        if self.wheels is not None:
            for wheel in self.wheels:
                wheel.stop()

# let's create a car with engine and wheels
# first we need to create an engine
engine = Engine(200)
# then we need to create wheels
wheels = [Wheel(18) for _ in range(4)] # _ means we do not care about the value

# now we can create a car
my_car = Car("Audi", "A4", 2020, engine, wheels)

# let's start the car
my_car.start()

# I could turn an individual wheel if I wanted
# so let's turn the first wheel
my_car.wheels[0].turn()

# let's stop the car
my_car.stop()

# composibility is a powerful concept

# one potential issue is how do properties of the engine and wheels get updated
# how do objects inside communicate with each other?
# we then have to write methods that will do that
