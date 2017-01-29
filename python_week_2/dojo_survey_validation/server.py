from flask import Flask, render_template, request, redirect,session,flash
app = Flask(__name__)
app.secret_key = "Why do we do this..."
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/result', methods = ['post'])
def results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    error = False
    if len(name) <1:
        error = True
        flash('Fill out the name please','name')
    if len(location) <1:
        error = True
        flash('Fill out the location please','location')
    if len(language) <1:
        error = True
        flash('Fill out the language please','language')
    if len(comment) <1:
        error = True
        flash('Comment Please','comment')
    if len(comment) >120:
        error = True
        flash('Comment to large to display','comment')
    if not error:
        return render_template('results.html',name = name, location = location, language = language, comment = comment)
    return redirect('/')
app.run(debug=True)
