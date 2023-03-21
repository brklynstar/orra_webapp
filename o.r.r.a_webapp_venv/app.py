from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def homepage():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__=='__main__':
    app.run(debug=True)