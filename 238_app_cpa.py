from flask import Flask 

app = Flask(__name__) 

@app.route("/")
def home_page(): 
    return "<h1>Welcome to SVG</h1>"

@app.route("/courses/<course_id>")
def course_page(course_id): 
    try: 
        n = int(course_id)
        if n not in [102, 106, 103, 601]: 
            return "<h1>Invalid course id</h1>"
    except: 
        return "<h1>Course id should be a valid number</h1>"
    
    return "<h1>Welcome to course page of {}".format(course_id)

@app.route("/login/<student_name>/<student_id>") 
def student_page(student_name, student_id): 
    if not student_name.isalpha(): 
        return "<h1>Student Name must be a alphabetic string</h1>"
    
    try: 
        st_id = int(student_id)
        if st_id not in range(1, 201): 
            return "<h1>Student id must be between 1 to 200</h1>"
    except: 
        return "<h1>Student id should be a valid number</h1>"
    
    return "<h1>Good morning {}, your id {} is verified".format(student_name, student_id)

@app.route("/about")
def about_page():
    return "<h1>Programming</h1>"

@app.route("/contact")
def contact_page():
    return "<h1>-@gmail.com</h1>"