#!/usr/bin/python3
""" module create basic Flask app """
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root_route():
    """ 'root' route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ 'hbnb' route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ 'c and text' route"""
    return "C" + " " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ 'python and text' route"""
    return "C" + " " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def num_route(n):
    """ "number"route """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template_route(n):
    """ "number_template" route """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even_route(n):
    """ "number_odd or even" route """
    result = str(n) + " "

    if n % 2 == 0:
        result = result + "is even"
    else:
        result = result + "is odd"
    return render_template("6-number_odd_or_even.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
