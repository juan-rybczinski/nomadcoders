from flask import Flask, render_template, request

app = Flask('SuperScrapper')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/report')
def report():
    word = request.args.get('word')
    return render_template('report.html', searchingBy=word)


# @app.route('/<username>')
# def contact(username):
#     return f'Hello {username}, how are you?'


app.run(host='127.0.0.1')
