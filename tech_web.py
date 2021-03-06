# -*- coding:utf-8 -*-
from flask import Flask, render_template, url_for, redirect,request

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
    # js中的语句
    return render_template('test06.html')

@app.route('/test07')
def js_test07():
    # js中的注释
    return render_template('test07.html')

@app.route('/test08')
def js_test08():
    # js中的变量
    return render_template('test08.html')

@app.route('/test09')
def js_test09():
    # js中的数据类型
    return render_template('test09.html')

@app.route('/test10')
def js_test10():
    # js中的对象
    return render_template('test10.html')

@app.route('/test11')
def js_test11():
    # js中的函数
    return render_template('test11.html')

@app.route('/test12')
def js_test12():
    # js中的事件
    return render_template('test12.html')

@app.route('/test13')
def js_test13():
    # js中的字符串
    return render_template('test13.html')

@app.route('/test14')
def js_test14():
    # js中的运算符
    return render_template('test14.html')

@app.route('/test15')
def js_test15():
    # js中的条件语句
    return render_template('test15.html')

@app.route('/test16')
def js_test16():
    # js中的循环
    return render_template('test16.html')

@app.route('/test17')
def js_test17():
    # js中的break continue
    return render_template('test17.html')

@app.route('/test18')
def js_test18():
    # js中的typeof
    return render_template('test18.html')

@app.route('/test19')
def js_test19():
    # js中的类型转换
    return render_template('test19.html')

@app.route('/test20')
def js_test20():
    # js中的类型转换
    return render_template('test20.html')

@app.route('/test21')
def js_test21():
    # js中的异常处理
    return render_template('test21.html')

@app.route('/test22')
def js_test22():
    # js中的变量提升
    return render_template('test22.html')

@app.route('/test23')
def js_test23():
    # js中的变量提升
    return render_template('test23.html')

@app.route('/test24')
def js_test24():
    # js中的常见误区
    return render_template('test24.html')

@app.route('/test25')
def js_test25():
    # js中的表单验证
    return render_template('test25.html')
@app.route('/test25_form',methods=["POST"])
def js_test25_form():
    # js中的表单验证2
    if request.method == 'POST':
        print('---------')
        print(request.form['myInput'])

@app.route('/test26')
def js_test26():
    # js中的json
    return render_template('test26.html')

@app.route('/test27')
def js_test27():
    # js中的void()
    return render_template('test27.html')
if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=8082)

