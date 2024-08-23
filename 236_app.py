from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index(): 
    return "<h1>Welcome to SVG Website</h1>" 

@app.route("/courses")
def course_page(): 
    return "<h1>Welcome to Information Page</h1>"

@app.route("/courses/106")
def python_page(): 
    return "<h1>Master in Python</h1>"

@app.route("/courses/103")
def cpp_page(): 
    return "<h1>Master in C++</h1>"

@app.route("/courses/102")
def c_page(): 
    return "<h1>Master in C</h1>"

@app.route("/courses/601")
def dsa_page(): 
    return "<h1>Master in DSA</h1>"
