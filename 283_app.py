from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("home.html")

@app.route("/<course_id>/<candidate_type>/<batch_timing>/<name>") 
def course_request(course_id, candidate_type, batch_timing, name): 
    if int(course_id) not in [102, 103, 106, 601]: 
        raise ValueError("Bad course id")
    
    if candidate_type not in ["student", "professional"]: 
        raise ValueError 
    
    if batch_timing not in ["morning", "evening"]: 
        raise ValueError 
    
    courses = {
                102:'Master in C', 
                103:'Master in C++', 
                106:'Master in Python', 
                601:'Master in DSA'
            }

    return render_template("course_request.html", course_name=courses[int(course_id)], candidate_type=candidate_type, 
                            batch_timing=batch_timing, name=name)