# we will use matplotlib to plot data from csv file
# csv file name will be temp_data.csv in current directory

import matplotlib.pyplot as plt
# if I do not have matplotlib installed I can install it using pip install matplotlib

# let's read data from file
# let's use csv module
import csv # standard Python
file_name = "temp_data.csv"
# data will be list of tuples
data = []
with open(file_name, "r", encoding="utf-8") as f:
    # we need to create csv reader
    reader = csv.reader(f)
    # we can now iterate over reader
    # each row will be a list of strings
    # we need to convert to float
    for row in reader:
        # skip header
        if row[0] == "Time":
            continue
        # convert to float
        row[1] = float(row[1])
        # add to data
        data.append(row)

# let's plot data
# we need to separate time and temperature
# we can use list comprehension
time = [row[0] for row in data]
temp = [row[1] for row in data]

# let's plot
# plt.plot(time, temp) # x axis is time, y axis is temp
# let's plot bar
plt.bar(time, temp, width=0.5) # width is optional
# let's show only every 10th x tick
plt.xticks(time[::10])
# rotate 45 degrees
plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature vs Time")
# i could save png here 
plt.savefig("temp_vs_time.png")
# next line will start interactive plot skip this if you want to save png only
plt.show() # by default this is interactive plot using tkinter

# maplotlib is very powerful
# for full docs go here:
# https://matplotlib.org/stable/contents.html