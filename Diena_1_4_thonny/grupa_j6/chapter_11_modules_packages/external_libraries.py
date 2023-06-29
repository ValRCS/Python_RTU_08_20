# we can import standard libraries
# we can import our own libraries
# finally we can import external libraries

# how do we find external libraries?
# we can search for them on the web
# most popular repository is https://pypi.org/
# Sturgeon's Law: 90% of everything is crap
# same goes for libraries
# we have some curated lists of libraries
# such as Awesome Python
# https://github.com/vinta/awesome-python

# to install we need pip - python package manager
# similar to npm for node.js
# composer for php
# maven for java

# so to install tqdm we need to run
# pip install tqdm in terminal - once

from tqdm import tqdm

total = 0
for i in tqdm(range(10_000_000)):
    total += i

print(total)

# we can use pip freeze to see what we have installed and save to a file
# usually we save to requirements.txt
# pip freeze > requirements.txt

# then I can install ALL packages from requirements.txt
# pip install -r requirements.txt
# might require sudo on linux - not necessarily

# finally we can have >= or <= or == or > or < or != in requirements.txt
# to specify version numbers

