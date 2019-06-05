from app import app, db
from flask import render_template

from app.models import Writing
from app.forms import WriteForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
   form = WriteForm()
   if form.validate_on_submit():
      text = form.text.data
      author = form.author.data 
      wordcount = len(text.split(" "))
      new_writing = Writing(writing=text, author=author, wordcount=wordcount)
      db.session.add(new_writing)
      db.session.commit()
   return render_template('index.html', title='Writing', form=form)

@app.route('/writing')
def writing():
   writings = Writing.query.all()
   return render_template('writing.html', title='Writings', writings=writings)