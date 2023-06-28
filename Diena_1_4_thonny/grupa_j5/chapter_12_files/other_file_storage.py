# so we could save data in a regular text file
# then it is up to us to figure a format to save the data

# Python offers many other ways to save data
# we will look at some of them

# pickle - python object serialization
import pickle
import os
import Robot
import json
import pandas as pd
import sqlite3

# let's change our working directory to chapter_12_files
os.chdir('Diena_1_4_thonny/grupa_j5/chapter_12_files')

# let's create a list of numbers
numbers = [1, 2, 3, 4, 5]
# let's save it to a file
# note wb - write binary mode
# all modes here: https://docs.python.org/3/library/functions.html#open
with open('numbers.pickle', mode='wb') as f:
    pickle.dump(numbers, f)
# file is closed here
# pickle is great for saving any python object - but it is not human readable

# let's read the file
# notice rb - read binary mode
with open('numbers.pickle', mode='rb') as f:
    numbers_loaded = pickle.load(f)
# file is closed here
print(numbers_loaded)

# let's try make some Robot objects and then save them to a file
robot_dictionary = {}
robot_dictionary['r1'] = Robot.Robot('R1', 2020)
robot_dictionary['r2'] = Robot.Robot('Džonijs', 2021)
robot_dictionary['r3'] = Robot.Robot('R3', 2022)

# let's save it to a file
with open('robots.pickle', mode='wb') as f:
    pickle.dump(robot_dictionary, f)
# file is closed here

# let's read the file
with open('robots.pickle', mode='rb') as f:
    robots_loaded = pickle.load(f)
# file is closed here
print(robots_loaded)
# so we have a dictionary that holds 3 Robot objects

# if we want to use load our robot objects we need to import Robot class first
# pickle can be used for anything - except classes, functions and methods

# json - JavaScript Object Notation
# json is a text format that is completely language independent
# invented by Douglas Crockford at Yahoo in 2001
# site with json info: https://www.json.org/json-en.html
# most widely used format for data exchange among different programming languages and systems

# so let's make a list of dictionaries
new_robot_list = []
for robot in robots_loaded:
    # for each robot in robots_loaded we will add a dictionary to new_robot_list
    new_robot_list.append(robots_loaded[robot].get_dictionary())

print(new_robot_list)

# let's save this to JSON file
with open('robots.json', mode='w', encoding="utf-8") as f:
    json.dump(new_robot_list, f, ensure_ascii=False, indent=4)
    # indent is for looks - it will make the file more readable
    # ensure_ascii=False - this is for non-ascii characters to show up correctly

# let's read the file
with open('robots.json', mode='r', encoding="utf-8") as f:
    robots_data_loaded = json.load(f)

print(robots_data_loaded)

# we could have loaded robots.json as string but that would not be very useful
# we would have to parse the string to get the data we need
with open('robots.json', mode='r', encoding="utf-8") as f:
    robots_data_loaded_string = f.read()
print(robots_data_loaded_string)

# we could even save data in a sqlite database
# sqlite is a lightweight relational database management system
# most popular database in the world - built in browsers, mobile phones, etc.
# included in python standard library
# https://www.sqlite.org/index.html

# let's import sqlite3
# import sqlite3
# let's connect to a database
# if the database does not exist it will be created
# if it exists it will be opened
# if we want to create a new database we can use :memory: as the database name

# let's connect to a database

conn = sqlite3.connect('robots.db')

# let's create a cursor
c = conn.cursor()

# let's create a table
c.execute('''CREATE TABLE IF NOT EXISTS robots
                (name text, build_year integer)''')

# let's insert some data
c.execute("INSERT INTO robots VALUES ('R1', 2020)")
c.execute("INSERT INTO robots VALUES ('Džonijs', 2021)")
c.execute("INSERT INTO robots VALUES ('R3', 2022)")

# let's save the changes
conn.commit() # commit is needed to save the changes
# more on how to work with sqlite3 in python: https://docs.python.org/3/library/sqlite3.html

# finally how to save data in a csv file
# csv - comma separated values
# unfortunately not all csv files are comma separated
# not a real standard

# let's import csv
# import csv
# i prefer pandas


# let's create a dataframe
df = pd.DataFrame({'name': ['R1', 'Džonijs', 'R3'],
                     'build_year': [2020, 2021, 2022]})
print(df)
# let's save to csv
df.to_csv('robots.csv', index=False)

# we can read the csv file
df_read = pd.read_csv('robots.csv')
print(df_read)

# we could also save to excel but we need pip install openpyxl
df.to_excel('robots.xlsx', index=False)

# other options would be to save to a different database
# also possible YAML, XML, etc.