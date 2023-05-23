#!/usr/bin/python3
"""A script that starts a Flask web application"""
fromm flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    """Returns a hello message"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """returns a string"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """Returns a string according to the argument passed"""
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=True)
