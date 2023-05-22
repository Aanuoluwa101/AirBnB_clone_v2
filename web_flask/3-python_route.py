#!/usr/bin/python3
"""A script that starts a Flask web application"""
from web_flask.__init__ import app


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


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """Returns a string according to the argument passed"""
    if text:
        return "Python " + text.replace("_", " ")
    else:
        return "Python " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
