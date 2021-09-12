#!/usr/bin/python3
""" module start Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ "cities_by_states" route. Send a correspond template."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ run before app would be closed """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
