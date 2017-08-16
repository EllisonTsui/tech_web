# -*- coding:utf-8 -*-
from flask import Flask, render_template, session, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=8082)
