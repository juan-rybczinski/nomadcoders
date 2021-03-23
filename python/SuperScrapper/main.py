from flask import Flask

app = Flask('SuperScrapper')


@app.route('/')
def home():
    return "Hello! Wecome to my home"


app.run(host='127.0.0.1')
