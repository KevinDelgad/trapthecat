import os

from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import function

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"