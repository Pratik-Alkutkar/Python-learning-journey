from flask import Flask 
from flask import render_template 

registered_users = ['pratik', 'rohit', 'radhika']

app = Flask(__name__)

@app.route("/")
def index(): 
    return "<h1>Hello, World</h1>"

@app.route("/user/<name>")
def user_page(name): 
    return render_template("user.html", name=name, reg_users=registered_users)