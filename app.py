from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    context = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=datetime.now)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/blog.html')
def blo():
    return render_template('blog.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blogs.html')
def blogss():
    blogs = Blog.query.filter().all()
    blogs.sort(reverse=True)
    return render_template('blogs.html', blogs=blogs)

@app.route('/delete', methods=['POST'])
def delete_movie():
    id=request.form['movie_to_delete']
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    blogs = Blog.query.filter().all()
    blogs.sort(reverse=True)
    return render_template('blogs.html', blogs=blogs, message=blog)

@app.route('/index.html')
def inde():
    return render_template('index.html')
@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method=='POST':
        title = request.form['title']
        context = request.form['context']
        blog = Blog(title=title, context=context)
        db.session.add(blog)
        db.session.commit()
        message = 'Blog added successfully'
        return render_template('blog.html', message=message)



if __name__ == '__main__':
    app.run()

