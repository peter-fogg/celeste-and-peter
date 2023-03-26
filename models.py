import flask as f
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    coming = db.Column(db.Boolean)
    bus = db.Column(db.Integer)
    diet = db.Column(db.String)
