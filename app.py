from flask import Flask, render_template, request

# creating an instance of Flask class
# needed so that Flask knows where to look for resources such as templates and static files
app = Flask(__name__)

# route() decorator to tell Flask what URL should trigger our function
@app.route("/", methods = ['GET', 'POST'])
# function returns message we want to display in the user's browser
def index_page():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        data = request.form
        print(data+'\n')
        return render_template("index.html")



