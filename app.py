from flask import Flask, render_template

# creating an instance of Flask class
# needed so that Flask knows where to look for resources such as templates and static files
app = Flask(__name__)

# route() decorator to tell Flask what URL should trigger our function
@app.route("/")
# function returns message we want to display in the user's browser
def hello_world():
    return render_template("index.html")



