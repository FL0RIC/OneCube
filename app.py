#--------------------------------#
#            Imports             #
#--------------------------------#

from flask import Flask, render_template

#--------------------------------#
#              Code              #
#--------------------------------#

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Login")
def login():
    return render_template("login.html")

@app.route("/Help")
def help():
    return render_template("help.html")

@app.route("/MyCube")
def myCube():
    return render_template("mycube.html")


app.run()