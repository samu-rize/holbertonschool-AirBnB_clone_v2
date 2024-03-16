#!/usr/bin/python3

"""
Flask application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a message to the user"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a message to the user"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display a message to the user"""
    if ("_" in text):
        text = text.replace("_", " ")

    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    """Run the main program"""
    app.run(host='0.0.0.0', port=5000)
