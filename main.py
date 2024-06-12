from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost/courses'
db = SQLAlchemy(app)

class Registration(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(75),nullable=False)
    email = db.Column(db.String(75),nullable=False)
    password = db.Column(db.String(75),nullable=False)
    # date = db.Column(db.DateTime, default=datetime.utcnow)

db.create_all()

@app.route('/',methods=['GET','POST'])
def Home():
    if (request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
       
        a = Registration(name=name,email=email,password=password)
        db.session.add(a)
        db.session.commit()
    return render_template('index.html')
@app.route('/about')
def About():
    return render_template('About.html')

@app.route('/course')
def course():
    return render_template('Course.html')

@app.route('/blog')
def Blog():
    return render_template('Blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/post1')
def post1():
    return render_template('post1.html')

@app.route('/post2')
def post2():
    return render_template('post2.html')

@app.route('/courseinner1')
def courseinner1():
    return render_template('courseinner1.html')

@app.route('/courseinner')
def courseinner():
    return render_template('courseinner.html')

@app.route('/cssinner')
def cssinner():
    return render_template('cssinner.html')

@app.route('/reactinner')
def reactinner():
    return render_template('reactinner.html')
@app.route('/jsinner')
def jsinner():
    return render_template('jsinner.html')
@app.route('/sqlinner')
def sqlinner():
    return render_template('sqlinner.html')

app.run(debug=True)
