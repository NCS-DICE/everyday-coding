from app import db

class Writing(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   author = db.Column(db.String(120))
   writing = db.Column(db.String(10000))
   wordcount = db.Column(db.Integer)