"""File contains flask server"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return "This is a test."

'''
TO DO:

'''
