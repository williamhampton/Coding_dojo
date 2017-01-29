from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")
@app.route("/ninjas")
def ninja():
    return render_template("ninja.html")
@app.route("/dojos/new")
def dojo():
    return render_template("dojo.html")
app.run (debug = True)
