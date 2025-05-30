from app import db
from .Role import Role

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
  last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
  recovery_code = db.Column(db.String(200), nullable=True)
  active = db.Column(db.Integer, default=1, nullable=True)

  role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
