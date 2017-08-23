# -*- coding:utf-8 -*-
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# tutorial section 01: javascript
@app.route('/')
def hello_world():
    return redirect(url_for('js_test01')) #url_for的参数要是路径对应的“方法名”

@app.route('/test01')
def js_test01():
    # 首次在前端添加javascript的效果提示
    return render_template('test01.html')

@app.route('/test03')
def js_test03():
    # js中document输出流
    return render_template('test03.html')

@app.route('/test04')
def js_test04():
    # js中的输出
    return render_template('test04.html')

@app.route('/test05')
def js_test05():
    # js中的语法
    return render_template('test05.html')

@app.route('/test06')
def js_test06():
    # js中的语法
    return render_template('test06.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=8082)
