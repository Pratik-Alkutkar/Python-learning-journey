from flask import Flask 
from flask import render_template 

app = Flask(__name__)

@app.route("/")
def index(): 
    return "<h1>Hello</h1>"

@app.route("/user/<name>")
def user_page(name): 
    return render_template("user.html", name=name)