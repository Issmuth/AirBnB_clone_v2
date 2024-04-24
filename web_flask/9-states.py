#!/usr/bin/python3
"""States."""
from models import storage
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
states = storage.all('State')



@app.route('/states', strict_slashes=False)
def states():
    """list states."""
    return (render_template('9-states.html', states=states))


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """list state by ID."""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        db = 1
    else:
        db = 0

    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state, db=db)

    return render_template('9-states.html', state=0)


@app.teardown_appcontext
def clear(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
