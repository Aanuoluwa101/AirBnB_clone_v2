#!/usr/bin/python3
"""A script that starts a Flask web application"""
from web_flask.__init__ import app
from flask import render_template


@app.route('/states_list')
def states():
    """Displays an html page"""
    return render_template('7-states_list.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
