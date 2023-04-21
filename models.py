import flask as f
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    has_plus_one = db.Column(db.Boolean)
    has_rehearsal_invite = db.Column(db.Boolean)

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))
    coming = db.Column(db.Boolean)
    bus = db.Column(db.Boolean)
    diet = db.Column(db.String)
    plus_one = db.Column(db.Boolean)
