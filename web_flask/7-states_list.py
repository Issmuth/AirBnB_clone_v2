#!/usr/bin/python3
"""Flask Integration."""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def listStates():
    """Lists the states."""
    states = storage.all("State")
    return (render_template('7-states_list.html', states=states))


@app.teardown_appcontext
def clear(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
