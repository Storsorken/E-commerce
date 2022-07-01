from time import sleep
import flask
from flask import request, render_template, redirect, url_for, g, flash, session
app = flask.Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "test" and password == "test":
            return redirect(url_for("index"))
        return "Invalid username or password"

    return render_template("login.html")
