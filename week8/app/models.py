# Get our database
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# MODELS without classes
followers = db.Table('followers', 
   db.Column('follower_id', db.Integer, db.ForeignKey('user.id')), 
   db.Column('follower_id', db.Integer, db.ForeignKey('user.id'))   
)

class User(UserMixin, db.Model): # Notice, this class now inherits from two parent classes.
   """
   This class extends the database Model, inheriting its attributes and methods.
   It will be a database model (or a table) for our users.
   """
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), index=True, unique=True)
   email = db.Column(db.String(120), index=True, unique=True)
   password_hash = db.Column(db.String(128)) # notice this isn't password, but password hash. This means we hash, or encrypt our passwords.
   followed = db.relationship(
      'User', secondary=followers,
      primaryjoin=(followers.c.follower_id == id),
      secondaryjoin=(followers.c.follower_id == id),
      backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
   )

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
   
   def follow(self, user):
      if not self.is_following(user):
         self.followed.append(user)
   
   def unfollow(self, user):
      if self.is_following(user):
         self.followed.remove(user)
   
   def is_following(self, user):
      return self.followed.filter( 
         followers.c.followed_id == user.id).count() > 0

   def followed_posts(self):
      followed = Posts.query.join(
         followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
      own = Posts.query.filter_by(user_id=self.id)
      return followed.union(own).order_by(Post.timestamp.desc())

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




