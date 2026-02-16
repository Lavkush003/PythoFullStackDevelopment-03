
# # # from flask import Flask

# # # app = Flask(__name__)

# # # @app.route("/")
# # # def home():
# # #     return "Flask Working Properly!"

# # # if __name__ == "__main__":
# # #     app.run(debug=True)





# # from flask import Flask, render_template

# # app=Flask(__name__)

# # @app.get('/')
# # @app.get('/home')
# # def home():
# #     return render_template("index.html", name="BOBTHEDOG")



# # @app.get('/about')

# # def about():
# #     return render_template("about.html", ab="It's about")



# # @app.get('/login')

# # def login():
# #     return render_template("login.html", log="Hello Bob")


# # @app.get('/contact')

# # def contact():
# #     return render_template("contact.html", cd="contact us")




# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")
#         print(email, password)
#         return "Login Successful (for now)"
#     return render_template("login.html")

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
