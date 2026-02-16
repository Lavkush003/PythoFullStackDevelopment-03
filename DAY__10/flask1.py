


from flask import Flask, jsonify, request, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def home():
    name=request.args.get("name", "Flask")
 

    return  render_template("index.html")


@app.route('/custom')
def custom():
    name=request.args.get("para","cus")
    name=name.replace("<", " ")
    name=name.replace(">", " ")
    name=name.replace("/", " ")

    return f" Hello, {(name)}"

#about page
@app.route("/about")
def about():
    return{
        "name":"Robin",
        "age": 21

    } 



#contact page

@app.route("/contact")
def contact():
    return "contact page"

#signup 
@app.route("/signup")
def signup():
    return "signup successfully", 402

app.run(debug=True,port=80)