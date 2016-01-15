from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
 
db = SQLAlchemy()

class Donkey(db.Model):
  __table__name = 'animal'
  animalID = db.Column(db.Integer, primary_key = True, unique = True)
  name = db.Column(db.String(100))
  regName = db.Column(db.String(100))
  breed = db.Column(db.Integer)
  sex = db.Column(db.Integer)
  height = db.Column(db.Integer)
  color = db.Column(db.String(50))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)