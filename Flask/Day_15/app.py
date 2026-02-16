
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/form")
def form():
    return render_template("form.html")


# Handle Form Submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")

    return render_template("display.html",
                           name=name,
                           email=email,
                           age=age)



@app.route("/form1", methods=["GET"])
def form1():
    name = request.args.get("name")  # Fetch data from GET request
    return render_template("form1.html", name=name)

if __name__=="__main__":
    app.run(debug=True)