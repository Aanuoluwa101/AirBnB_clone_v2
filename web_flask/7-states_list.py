#!/usr/bin/python3
"""A script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


all_states = storage.all(State)
if len(all_states) > 0:
    all_states = list(all_states.values())
    all_states.sort(key=lambda state: state.name)


@app.route('/states_list')
def states():
    """Displays an html page"""
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
