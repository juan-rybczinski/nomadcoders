from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask('SuperScrapper')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect('/')

    return render_template('report.html', searchingBy=word)


# @app.route('/<username>')
# def contact(username):
#     return f'Hello {username}, how are you?'


app.run(host='127.0.0.1')
