import os

from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import function

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, '/var/database.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/create-account")
def create_account():
    return 200