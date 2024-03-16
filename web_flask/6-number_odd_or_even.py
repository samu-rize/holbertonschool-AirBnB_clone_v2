#!/usr/bin/python3

"""
Flask application for routing.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays a welcome message."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of 'text'."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text='is_cool'):
    """Displays 'Python' followed by the value of 'text'."""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays a message indicating the provided number."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders a template with the provided number."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """Determines if the provided number is odd or even."""
    return render_template(
        '6-number_odd_or_even.html',
        n=n,
        result='even' if n %
        2 == 0 else 'odd')


if __name__ == '__main__':
    """Runs the Flask application."""
    app.run(host='0.0.0.0', port=5000)
