#!/usr/bin/python2
# coding=utf-8
# @Date: 7/15/18
# @Author: HZH
"""

"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)