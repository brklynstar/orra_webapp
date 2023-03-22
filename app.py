from datetime import datetime
from flask import Flask, render_template, url_for , flash , redirect ,
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

# configs
app = Flask(__name__)
app.config['SECRET_KEY'] = '57845b6f75838a78a5c99328a30eadd9'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# models

class User(db.Model):
    id = db.Column(db.Integar, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # query running in background that will get all users posts

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integar, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integar, db.ForeignKey('user_id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# dummy post code
posts = [
    {'author' : 'Brooke Finister',
    'title' : 'First post content',
    'date_posted' : 'March 20, 2023'},

    {'author' : 'Latoya Parra',
    'title' : 'Blog Post 2',
    'date_posted' : 'March 21, 2023'},
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register" , methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Success! Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password')

    return render_template('login.html', title = 'Login', form = form)



if __name__=='__main__':
    app.run(debug=True)

   