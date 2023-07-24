import random
import time # for sleep
from datetime import datetime # for timestamp

def return_temp(previous=None, hw_id=None) -> float:
    if hw_id is None:
        """Returns a random temperature between 0 and 100 degrees"""
        return random.randint(0, 100)
    else:
        # here would be code to read temperature from sensor
        # it would be a library provided by sensor manufacturer
        # for now we will just return a random number
        return random.randint(0, 100)
    

def main(file_name=None, hw_id=None, interval=5, n=None):
    # let's read temperature every 5 seconds so 0.2 Hz
    
    # setup let's open file
    if file_name is None:
        print("Sorry no file name provided")
        return # we need to have a file name
    
    # if we stick with ascii we do not need utf-8 but could add it
    with open(file_name, "w") as f:
        # write header
        f.write("Time, Temperature\n")
        while True:
            # read temperature
            temp = return_temp(hw_id=hw_id)
            # get timestamp
            timestamp = datetime.now()
            # format if you want using strftime
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            # write to file
            f.write(f"{timestamp}, {temp}\n")
            # flush to disk
            f.flush() # this will ensure that data is written to disk
            # sleep for interval
            time.sleep(interval)
            # decrement n
            if n is not None:
                n -= 1
                if n == 0:
                    break


if __name__ == "__main__":
    main(file_name="temp_data.csv", hw_id="1234", interval=1, n=30)
