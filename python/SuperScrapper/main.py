from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask('SuperScrapper')

db = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        from_db = db.get(word)
        if from_db:
            jobs = from_db
        else:
            jobs = get_jobs(word)
            db[word] = jobs

    else:
        return redirect('/')

    return render_template('report.html', searchingBy=word, resultsNumber=len(jobs))


# @app.route('/<username>')
# def contact(username):
#     return f'Hello {username}, how are you?'


app.run(host='127.0.0.1')
