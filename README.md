# tech_web notes
### tutorial section01:javascript ##
   1. [JavaScript动态效果初体验](http://127.0.0.1:8082/test01)
   2. [JavaScript的初步介绍](http://127.0.0.1:8082/test02)
>* html输出流写法document.write()及其页面加载后的区别;
>* js执行动作效果;
>* js获得元素document.getElementByXX以及修改元素信息
   3. [JavaScript的使用](http://127.0.0.1:8082/test03)
>* js代码涉及script标签的位置；
>* 引用外部js库的方式
   4. [JavaScript的输出](http://127.0.0.1:8082/test04)
>* 方式1:window.alert('infos')弹出警告框；
>* 方式2:document.write('infos')将内容写到html文档中
>* 方式3:通过innerHTML写入到Html元素中
>* 方式4:通过console.log()写入到浏览器的控制台

>    说明1：console调试相比较于alert()方式优越：其一不影响页面调试；其二可以显示更详细的结构信息；
>            document.write()是直接入到入到html页面中的，期间浏览器会自动调用documnet.open(),所以每次关闭write之后，页面会被重写；
>            而innerHTML是Dom页面元素的一个属性，代表元素精确的内容，写法是：document.(getElementByXX).innerHTML。
>    说明2：提及DOM:DOM(documnet object model)即文档对象模型，DOM是将文档描述成是一个树型结构。
   5. [JavaScript的语法](http://127.0.0.1:8082/test05)
> 语法包含内容如下：
>   * 字面量:数字字面量(3.14)、字符串字面量('hello')、表达式字面量(5+7)、数组字面量([1,2,3])、对象字面量({name:'xu',age:10})、函数字面量(function func(a){return a;})
>   * 变量:关键字var定义变量，等号用于变量赋值；(注意：字面量是定值；而变量通过变量名来获取，是可变的)
>   * 操作符:算术、赋值和位运算符；条件、比较以及逻辑运算符；（）
>   * 语句:即浏览器发出的命令 以分号分隔；
>   * 关键字:js也保留了一些关键字来标识需要执行的操作，不可以定义成变量名，比如var定义变量；以字母/下划线/美元符开始，后续字符可以是字母/数字/下划线/美元符
>   * 注释
>   * 数据类型：数字Number、字符串String、数组Array、对象Object等
>   * 函数： function func(){执行语句}
>   * 字母大小写敏感
>   * 字符集：js使用Unicode字符集
>   * js中常见的字符命名方式驼峰命名方式，如helloWorld
   6. [JavaScript的语句](http://127.0.0.1:8082/test06)
> * 语句作用无非是给浏览器发送指令，而每句指令给结尾添加英文分号'1'';
> * JS的代码是按照编码顺序进行执行，JS是脚本语言，浏览器读取代码是逐行执行脚本代码，而其他一些编程语言是会在代码执行前进行编译的，如java等;
> * JS代码块作用是一并执行的代码序列，以左右花括号进行组合 '{代码内容}';
> * 常用的语句标识符：break,catch,continue,do……while,for,for …… in ……，function，if …… else,return,switch,throw,try,var,while.
> * JS解释器会忽略多余空格，也可以在文本字符串中使用反斜杠进行换行，提高代码可读性。
   7. [JavaScript的注释](http://127.0.0.1:8082/test07)
> * 注释是不会被浏览器执行的，一般用于代码解释和调试
> * 单行注释   //
> * 多行(代码块)注释 /* 注释内容 */
   8. [JavaScript的变量](http://127.0.0.1:8082/test08)
> * JS的变量通过var来声明，形如 var 变量名，默认没有赋值的变量是undefined;
> * 可以同时声明多个变量 var 变量名1 = 1，变量名2 = '小明'
> * 需要说明的是，重新声明一个变量的时，变量值不变，比如：var name = 'xiaoming';var name   其值还是'xiaoming',除非重新定义。
   9. [JavaScript的数据类型](http://127.0.0.1:8082/test09)
> * JS的数据类型：数字(Number),数组(Array),布尔(Boolean),字符串(String),对象(Object),空(Null),未定义(Nndefined) ;
> * JS的类型是动态类型，即相同变量可用作不同的类型 ;
> * 数据类型——字符串:使用单引号或者是双引号均可，在一个字符串中有引号存在，可以用反斜杠进行转义 ;
> * 数据类型——布尔：true 和 false ,注意是小写;
> * 数据类型——数组：3种方式 new Array(), ['str1','str2'],new Array('str1','st2');
> * 数据类型——对象：有点类似字典,形如:var people = {'name':'xiaoming','age':25},寻址方式：people['name']或者people.name
> * 数据类型——Undefined:变量未初始化，就会赋予Undefined值
> * 数据类型——Null:用来表示尚未存在的对象，一般是对于获得的对象不存在的时候，返回的值
> * 声明变量时候，都要用关键字 new 进行声明;
> * 数据类型通过typeof来判断  写法:typeof 对象
   10. [JavaScript的对象](http://127.0.0.1:8082/test10)
> * JS的对象是属性和方法的容器 ;
> * JS的对象属性的调用方式两种：对象.属性  /  对象[属性]
> * JS的对象方法的调用方式: 对象.方法()  ,如果采用  对象.方法 的结果会将其后的方法处理成字符串输出
> * 总结：属性调用：对象.属性；方法调用：对象.方法()

