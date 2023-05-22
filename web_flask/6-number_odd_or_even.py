#!/usr/bin/python3
"""A script that starts a Flask web application"""
from web_flask.__init__ import app
from flask import render_template


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


@app.route('/number/<int:n>')
def number(n):
    """Returns a string"""
    return str(n) + " is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays a template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    """Displays a template file"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               number=n, status='even')
    else:
        return render_template('6-number_odd_or_even.html',
                               number=n, status='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
