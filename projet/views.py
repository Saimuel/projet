from projet import app
from flask import render_template, request

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template("login.html")
