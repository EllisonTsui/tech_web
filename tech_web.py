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

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=8082)
