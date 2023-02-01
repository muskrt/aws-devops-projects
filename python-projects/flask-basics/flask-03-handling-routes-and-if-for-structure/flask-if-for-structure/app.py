# Import Flask modules
from flask import Flask, render_template, url_for, redirect
# Create an object named app 
app = Flask(__name__)

# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route("/")
def head():
    first="welcome to the abc company"
    return render_template("index.html", message = first)


# Create a function named header which prints numbers elements of list one by one in `index.html` 
# and assign to the route of ('/')
@app.route('/devops-login')
def devops_login():
    return render_template("devops.html")

@app.route('/cloud-login')
def cloid_login():
    return render_template("cloud.html")

@app.route("/cloud-team")
def cloud_team():
    names =["Serdar", "Sam", "Jasper"]
    # numbers = range(1.11)
    return render_template("body.html", team = "cloud", object = names)

@app.route("/devops-team")
def devops_team():
    names =["Serdar", "Sam", "Jasper"]
    # numbers = range(1.11)
    return render_template("body.html", team= " devops" , object = names)


# run this app in debug mode on your local.
if __name__== "__main__":
    app.run(debug=True,port=5000)



