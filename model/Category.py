from extensions import db

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  description = db.Column(db.Text(), nullable=False)