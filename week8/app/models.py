# Get our database
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model): # Notice, this class now inherits from two parent classes.
   """
   This class extends the database Model, inheriting its attributes and methods.
   It will be a database model (or a table) for our users.
   """
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), index=True, unique=True)
   email = db.Column(db.String(120), index=True, unique=True)
   password_hash = db.Column(db.String(128)) # notice this isn't password, but password hash. This means we hash, or encrypt our passwords.

   def __repr__(self):
      """
      This tells the program how to print objects. One object will be a user. 
      Instead of printing the memory address, it will print the following string.
      """
      return '<User {}>'.format(self.username)

   def set_password(self, password):
      self.password_hash = generate_password_hash(password) # Create password hash
   
   def check_password(self, password):
      return check_password_hash(self.password_hash, password) # Check that the password matches the password hash
   

class Post(db.Model):
   """
   This class extends the database Model, inhereting its attributes and methods.
   It will be a database model (or a table) for our posts. It will connect to 
   the users via a foreign key.
   """
   id = db.Column(db.Integer, primary_key=True)
   body = db.Column(db.String(140))
   timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # This will link entries on this table to entries in the users table by user id.

   def __repr__(self):
      return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
   return User.query.get(int(id))
   