#!/usr/bin/python3
"""First flask application."""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns string."""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns another string."""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
