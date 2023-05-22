#!/usr/bin/python3
"""A script that starts a Flask web application"""
from web_flask.__init__ import app


@app.route('/')
def say_hello():
    """Returns a hello message"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
