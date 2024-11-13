# let's make a simple hello world flask app

from flask import Flask

app = Flask(__name__)

# let's make a route for the root of the website as well as for /hello
@app.route("/")
def home():
    return "Welcome to the home page!"

# now we define the route for /hello on our website
@app.route("/hello")
def hello():
    return "Hello, World!"

# let's add a greeting route which allows custom greetings
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

# let's make a random number generator that returns JSON
import random
from flask import jsonify

@app.route("/random_number")
def random_number():
    # so I pass Python dictionary to jsonify function
    number = random.randint(1, 100)
    return jsonify({"number": number})

# let's make a route that returns a list of numbers
@app.route("/numbers")
def numbers():
    numbers = [random.randint(1, 100) for _ in range(10)]
    return jsonify({"numbers": numbers})

# we can also render templates
# docs https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates
from flask import render_template

@app.route('/sveiks/')
@app.route('/sveiks/<name>')
def sveiks(name=None):
    return render_template('hello.html', person=name)

# now we could also add database support meaning we could store data in a database
# then when someone visits the website we could show them data from the database

# let's add a route that returns a list of names
@app.route("/names")
def names():
    names = ["John", "Jane", "Jack", "Jill"] # this could be data from a database
    # so you would have to call the database here
    return jsonify({"names": names})

# flask also lets us have authorization and authentication

# to run the app we need to call the run method
if __name__ == "__main__":
    app.run(debug=True)