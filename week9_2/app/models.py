from datetime import datetime
# For password hashing
from werkzeug.security import generate_password_hash, check_password_hash
# For login business
from flask_login import UserMixin
# For hashmaking
from hashlib import md5

# Get our database, and login manager
from app import db, login

# classless tables
followers = db.Table('followers',
   db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
   db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

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
   posts = db.relationship('Post', backref='author', lazy='dynamic') #IMPORTANT this line is skipped in the tutorial
   about_me = db.Column(db.String(140))
   last_seen = db.Column(db.DateTime, default=datetime.utcnow)
   followed = db.relationship(
      'User', secondary=followers,
      primaryjoin=(followers.c.follower_id == id),
      secondaryjoin=(followers.c.followed_id == id),
      backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

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
      followed = Post.query.join(
         followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
      own = Post.query.filter_by(user_id=self.id)
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
