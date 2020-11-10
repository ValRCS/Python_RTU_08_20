def tool_fun(argument):
    print(f"Did you come here for an {argument}")

def complex_fun(a,b):
    return a*b

if __name__ == "__main__":
    # so runs only when my_tools.py is run as main meaning python my_tools.py
    # good place for tests
    print(f"Starting library tests for {__file__}")
    assert(30 == complex_fun(5,6))
    # more tests for our functions