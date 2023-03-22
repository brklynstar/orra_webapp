from flask import Flask, render_template, url_for , flash , redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '57845b6f75838a78a5c99328a30eadd9'

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

   