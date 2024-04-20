#!/usr/bin/python3
"""More routing and Flask intro."""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns hello hbnb."""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns hbnb."""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns C followed by a the string."""
    return ('C {}'.format(escape(text.replace('_', ' '))))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
