from datetime import datetime
# For password hashing
from werkzeug.security import generate_password_hash, check_password_hash
# For login business
from flask_login import UserMixin
# For hashmaking
from hashlib import md5

# Get our database, and login manager
from app import db, login

# classless functions
#This runs the function through the user_loader method
@login.user_loader
def load_user(id):
   return User.query.get(int(id))

class User(UserMixin, db.Model):
   """
   This class extends the database Model, inheriting its attributes and methods.
   It will be a database model (or a table) for our users.
   """
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), index=True, unique=True)
   email = db.Column(db.String(120), index=True, unique=True)
   password_hash = db.Column(db.String(128)) # notice this isn't password, but password hash. This means we hash, or encrypt our passwords.
   about_me = db.Column(db.String(140))
   last_seen = db.Column(db.DateTime, default=datetime.utcnow)
   
   def __repr__(self):
      """
      This tells the program how to print objects. One object will be a user. 
      Instead of printing the memory address, it will print the following string.
      """
      return '<User {}>'.format(self.username)

   # Create a hashed password
   def set_password(self, password):
      self.password_hash = generate_password_hash(password)

   # Check password against hashed password
   def check_password(self, password):
      return check_password_hash(self.password_hash, password)

   def avatar(self, size):
      digest=md5(self.email.lower().encode('utf-8')).hexdigest()
      return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
   
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
