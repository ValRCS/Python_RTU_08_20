# i could store just regular functions here

def say_hi(name):
    print(f"Hi, I am {name}")

def say_bye(name):
    print(f"Bye, bye, {name}")

# make utility functions
def pretty_name(name):
    return name.title().replace("_", " ")

# i could add main guard here too
if __name__ == "__main__":
    print("This is the my_functions module run directly")
    # let's test some functions
    say_hi("Marvin")
    say_hi("Alice")
    print(pretty_name("marvin"))
    print(pretty_name("alice"))
    print(pretty_name("marvin_the_robot"))
    # let's check if we can access x's name
    assert pretty_name("marvin_the_robot") == "Marvin The Robot" # simple sanity check