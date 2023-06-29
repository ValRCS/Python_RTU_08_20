# Python supports wide variety of file formats:
# csv, json, xml, html, pdf, docx, xlsx, png, jpg, mp3, mp4, ...
# for some we need external libraries - pandas, openpyxl, ...

# first let's look at using pickle to save and load Python objects
# first we need to import pickle
import pickle
from robot import Robot

# let's make a list of dictionaries holding person data

dict_list = [
    {"name": "John", "surname": "Smith", "age": 25},
    {"name": "Jane", "surname": "Doe", "age": 30},
    {"name": "Jack", "surname": "Black", "age": 35},
    {"name": "Jill", "surname": "White", "age": 40},
]

# let's save it to a file
# we will use relative path
# note wb - write binary, no encoding needed
with open("data/persons.pickle", mode='wb') as fstream:
    # file is open here
    # we will use pickle.dump to save the object
    pickle.dump(dict_list, fstream)
    # file is still open here
# file is closed here - no need to close it manually!

# let's load it back - i could do it from another script/program
# we will use relative path
# note rb - read binary
with open("data/persons.pickle", mode='rb') as fstream:
    # file is open here
    # we will use pickle.load to load the object
    loaded_dict_list = pickle.load(fstream)
    # file is still open here
# file is closed here - no need to close it manually!

# let's print it
print(loaded_dict_list)

# pickle is a binary format - not human readable!
# also not secure - do not use it for sensitive data!
# you would need to encrypt afterwards if you need to secure it

# let's make a list of 5 robots
robot_list = []
for i in range(5):
    robot_list.append(Robot(f"Robot {i+1}", build_year= 2020 + i))

print(robot_list)
# now let us pickle our robot list
# we will use relative path
# note wb - write binary, no encoding needed
with open("data/robots.pickle", mode='wb') as fstream:
    # file is open here
    # we will use pickle.dump to save the object
    pickle.dump(robot_list, fstream)
    # file is still open here
# file is closed here - no need to close it manually!

# now let's save dictionary from each robot to json file

# json is a text format - human readable !
# invented by Douglas Crockford from Yahoo! in 2001 - based on Javascript
# has some similarities to Python dictionaries and lists
# json has overtaken xml as the most popular data exchange format
# among different programming languages and it systems

# let's import json
import json # should go up top

# let's make a list of dictionaries holding robot data
dict_list = []
for robot in robot_list:
    dict_list.append(robot.get_dict())
print(dict_list)

# let's save it to a json file 
# we will use relative path

# note w - write, no encoding needed
with open("data/robots.json", mode='w', encoding="utf-8") as fstream:
    # file is open here
    # we will use json.dump to save the object
    json.dump(dict_list, fstream, indent=4, ensure_ascii=False)
    # indent is for looking pretty
    # ensure_ascii=False is for non-ascii characters to be displayed correctly
    # file is still open here
# file is closed here - no need to close it manually!

# now let's read it back
# we will use relative path

# note r - read, no encoding needed
with open("data/robots.json", mode='r', encoding="utf-8") as fstream:
    # file is open here
    # we will use json.load to load the object
    loaded_dict_list = json.load(fstream)
    # file is still open here
# file is closed here - no need to close it manually!
print(loaded_dict_list)

# for XML we can use ElementTree
# will not go into today

# for CSV we can use csv module
import csv # should go up top
# let's save our robot list to csv file
# we will use relative path
# note newline='' - to avoid blank lines
with open("data/robots.csv", mode='w', newline='') as fstream:
    # file is open here
    # we will use csv.writer to save the object
    csv_writer = csv.writer(fstream)
    # first we need to write the header row
    csv_writer.writerow(["name", "build_year"])
    # now we can write the data rows
    for robot in robot_list:
        csv_writer.writerow([robot.name, robot.build_year])
    # file is still open here
# file is closed here - no need to close it manually!

# there is no standard for csv - you can use any delimiter etc

# now let's read it back
# i will use pandas library which is great for tabular data
# we will use relative path

# note r - read, no encoding needed
import pandas as pd # should go up top
# let's read it back
# ingore index column
# read_csv has many options - check documentation
# docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# because csv is a text format, we need to specify encoding
df = pd.read_csv("data/robots.csv", index_col=0)
print(df)

# now let's save our robot list to excel file
# we will use relative path
# note index=False - to avoid index column
# i will use pandas
# note sheet_name="robots" - to specify sheet name
# note engine="openpyxl" - to use openpyxl library
# note we need to install openpyxl library first with pip install openpyxl

# df.to_excel("data/robots.xlsx", sheet_name="robots", index=False, engine="openpyxl")
df.to_excel("data/robots.xlsx")

# Python also has built in support sqlite3 database
# sqlite3 is a lightweight database - no server needed
# up to 140TB of data in a single .db file
# most popular database in the world - used in all browsers, smartphones, ...
# used in many applications - Firefox, Chrome, Skype, iTunes, ...

import sqlite3 # should go up top
# let's connect to our database
# we will use relative path
# note if database does not exist, it will be created

db = sqlite3.connect("data/robots.db") 
# now we have a connection object
# we can use it to execute sql commands
# we will use cursor object
cursor = db.cursor()

# let's create a table
# note if table already exists, it will not be created

# note we need to use triple quotes for multiline strings
# note we need to use """ for multiline comments

sql = """
CREATE TABLE IF NOT EXISTS robots (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    build_year INTEGER)
"""
# now we can execute it
cursor.execute(sql)

# let's insert some data
# note we need to use triple quotes for multiline strings
# note we need to use """ for multiline comments

# lets loop our robot list
for robot in robot_list:
    # note we need to use f-string to insert variables into sql
    sql = f"""
    INSERT INTO robots (name, build_year) 
    VALUES ("{robot.name}", {robot.build_year})
    """
    # NOT SAFE if you get data from user input - SQL injection attack!!!
    # use ? instead of variables
    # now we can execute it
    cursor.execute(sql)

# let's commit our changes
db.commit()

# for more extensive database work, use SQLAlchemy library 
# https://www.sqlalchemy.org/
