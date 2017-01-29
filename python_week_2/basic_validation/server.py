from flask import Flask, render_template, redirect, request, session,flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
  if len(request.form['name']) < 1:
      flash("Error name can not be empty")
  else:
      flash("Your name is {}".format(request.form['name']))
  return redirect('/')
app.run(debug=True)
