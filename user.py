import os

from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy

import dataclasses



@dataclasses.dataclass
class Newuser:
    first_name: str
    last_name: str
    user_name: str
    password: str

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db.init_app(app)

class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Welcome to Trap the Cat!</p>"

@app.route("/create-account", methods=["POST"])
def create_account():
    values = request.get_json()
    user = User(
        username = values["user"],
        password = values["password"],
        first_name = values["first_name"],
        last_name = values["last_name"]
    )
    db.session.add(user)
    db.session.commit()

    return user.username
