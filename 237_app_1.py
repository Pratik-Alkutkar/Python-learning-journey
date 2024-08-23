from flask import Flask 

app = Flask(__name__)

@app.route("/<name>")
def index(name): 
    return "<h1>Hello, Welcome to Home Page of {}</h1>".format(name)


"""
/home/pratik

home, pratik -> pathname component 
similar to pathname component there is a URL component 

if URL component is in <> then it is called as a dynamic component 
or dynamic route 
"""