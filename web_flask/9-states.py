#!/usr/bin/python3
""" module start Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def cities_by_states(id=None):
    """ "states" route and subroute. send a correspond template."""
    states = storage.all(State)
    state = None

    try:
        if id is not None:
            id = "State." + id
            state = states[id]
        else:
            states = states.values()
            state = None
    except:
        state = None
        states = None

    return render_template('9-states.html', states=states, state=state)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ run before app would be closed """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
