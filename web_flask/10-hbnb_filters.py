#!/usr/bin/python3
"""incorporate the web static project."""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
states = storage.all('State')
amenities = storage.all('Amenity')


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """filter jinja templates."""
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def clear(exc):
    """clears session after query."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
