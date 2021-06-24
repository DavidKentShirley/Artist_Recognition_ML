# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:52:55 2021

@author: XD
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"


if __name__ == "__main__":
    app.run(port=5000)