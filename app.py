from flask import Flask, render_template, request


api_key = 'unwIttz59iNAXrLsiHSwV0n3Wrb8hKR0nm4TMq2D'
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
        location = data.getlist('location')
        budget = data.getlist('budget')
        satread = data.getlist('SATread')
        satmath = data.getlist('SATmath')
        act = data.getlist('ACT')

        size = data.getlist('size')

        #print(data.getlist('location'))
        print(location, budget, satread, satmath, act, size)
        
        return render_template("index.html")




@app.route("/collage", methods = ['GET', 'POST'])
def collage_page():
    if request.method == 'GET':
        return render_template("collage.html")

    if request.method == 'POST':
        
        
        return render_template("collage.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
