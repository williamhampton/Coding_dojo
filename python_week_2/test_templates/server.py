
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html", phrase="Hello", times=7)
app.run(debug=True)
