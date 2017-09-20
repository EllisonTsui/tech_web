# tech_web notes
### tutorial section01:javascript ##
   1. [JavaScript动态效果初体验](http://127.0.0.1:8082/test01)
   2. [JavaScript的初步介绍](http://127.0.0.1:8082/test02)
>* html输出流写法document.write()及其页面加载后的区别;
>* js执行动作效果;
>* js获得元素document.getElementByXX以及修改元素信息
>* ECMAScript是JS的标准，后者是前者的实现；
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
> * 注释是不会被浏览器执行的，一般用于代码解释和调试;
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
> * JS的对象属性的调用方式两种：对象.属性  /  对象[属性];
> * JS的对象方法的调用方式: 参数.方法()  ,如果采用  对象.方法 的结果会将其后的方法处理成字符串输出;
> * 总结：属性调用：对象.属性；方法调用：对象.方法();
   11. [JavaScript的函数/作用域](http://127.0.0.1:8082/test11)
> * 函数是由事件驱动或者是被调用时可重复调用的方法块;
> * 语法：function func1(){需要执行的代码}，带参数的function myFunction(var1,var2){需要写的编码}，任意多的参数，由逗号','分隔,函数名不需要var定义，直接参数写就可以了;
> * function函数表达式；Function构造函数 也是定义函数的方式;
> * 提升(Hoisting) 可以将变量的声明和函数的声明提前，即可以在声明之前调用;
> * 函数自己调用 (function () {var x = "自我调用";})();
> * 函数显式参数和隐式参数,显式是指的定义时候的参数，而隐式参数是真实传输的数值;
> * 函数显式参数在定义时不指定数据类型,JS函数隐式参数不检测数据类型，也不进行参数个数检测，如果在调用时未给隐式参数提供值，就按照undefined来处理;
> * JS函数有内置对象arguments对象;
> * 强调一下,函数名是大小写敏感的;
> * return返回指定值,函数终止;
> * JS的局部变量，函数内部声明的变量(var声明)是局部变量,只能在函数内部访问，所以在不同的函数中可以命名相同的局部变量名，并且在函数运行完毕，内部变量会被销毁;
> * JS的全局变量，所有函数均可访问;
> * JS的函数参数，也是局部变量，仅仅只在当前函数中使用,值得注意的是:1对于值传递的参数不会修改传递进来的参数值，即函数内可见函数外不可见;2.对于对象传递,若修改对象的属性值，函数外的对象的属性值也被修改;
> * JS的变量生命周期，局部变量会在函数执行完毕后销毁，而全局变量会在页面关闭时销毁;
> * 如果将值赋予一个未声明的变量，则不管是否在函数内部，都是全局变量;
> * 对于JS中赋值的一些内容需要考虑解释型语言的顺序；
> * 补充说明：有关作用域的内容，如上所述，局部变量和全局变量的区别，其中，全局变量属于window变量，在JS中，对象和函数都属于变量;
> * 函数的4种调用方式：(在js中，函数可以看成是对象)，this指向函数执行的当前对象:1.直接调用（this就是全局对象，而html中的全局对象就是html页面本身，在浏览器中就是浏览器对象window对象，但是将window对象作为一个变量容易造成程序崩溃);2.函数作为方法调用(即在对象中定义函数);3.使用构造函数调用函数(即new 函数名())，此时构造函数中this没有任何值，只有在被调用的时候会被实例化；4.作为函数方法调用函数，call()和apply()，两个方法第一个参数是对象本身,区别就在于前者的参数和函数一致，而后者的参数是入参数组；
    12. [JavaScript的事件](http://127.0.0.1:8082/test12)
> * JS的事件作用于html元素上,可以是浏览器所为，也可以是用户触发所为;
> * 事件的实例：页面加载，
> * 常用html事件：onclick(用户点击)，onchange(html元素改变)，onmouseover(用户在一个HTML元素上移动鼠标),onmouseout(用户从一个HTML元素上移开鼠标),onkeydown(用户按下键盘按键),onload(浏览器已完成页面的加载)
   13. [JavaScript的字符串](http://127.0.0.1:8082/test13)
> * JS字符串用于存储一串字符;
> * JS的字符串使用双引号或者单引号;
> * 需要注意的是在字符串中也有引号时候，可以使用与字符串引号不一样的引号，或者使用反斜杠'\'进行转义，反斜杠将特殊符号转成字符串字符
> * 字符串也可是是对象，采用new String('john'),但typeof string对象 属于object,另外不建议创建String对象，会减慢执行速度;
> * 顺便提一下，== 是指的值相等，但是 === 是绝对相等，值和类型都相等;
   14. [JavaScript的运算符](http://127.0.0.1:8082/test14)
> * JS算术运算符（+ - * / % ++ --），对于取模，值的符号仅仅与被除数有关,JS中+运算符在字符串中的使用，可用于字符串连接，也可以用于字符串与数字的加法运算，但是最终是返回字符串，譬如'hello'+1  结果是'hello1';;
> * JS赋值运算符（= += -= *= /= %=）;
> * JS比较运算符（== === != !== > < >= <=）,其中!== 值和类型有一个不相等，或两个都不相等,需要注意的是 5 == ‘5’的值是true；
> * JS逻辑运算符（&& || ！）
> * JS条件运算符： 变量 = (条件)？value1:value2,如果条件满足结果为value1,不满足条件结果value2
   15. [JavaScript的条件语句](http://127.0.0.1:8082/test15)
> * 顾名思义就是根据不同的条件执行相应的代码块；
> * if /if...else /if...else if....else /switch
> * switch(n){case 1:代码块1; break; case 2:代码块2;break;default:与 case1和case2不同时执行的代码块;} 需要注意的是此处的break是用于防止执行的代码继续执行,跳出该case,当然也视情况而定;
   16. [JavaScript的循环](http://127.0.0.1:8082/test16)
> * JS四种循环方式 for /for in(循环遍历对象的属性,也遍历数组) /while/do while；
> * for(语句1；语句2；语句3){执行语句；}  语句1：初始值，语句2：条件语句， 语句3：循环后执行的语句；
> * for(语句1；语句2；语句3)语句1/2/3 均可以省略，但需要1：先前有初始化/ 2：要有循环终止条件，比如执行语句中有break/ 3:视情况而定  处理，不能够无限循环，导致浏览器崩溃；
> * for(x in 对象/数组){x //对象的话就是key,数组的话就是直接的值}
> * while(条件){执行代码;}只要条件允许，就执行代码；
> * do{}while();该语句会在执行条件语句之前执行一点代码块；
   17. [JavaScript的break、continue](http://127.0.0.1:8082/test17)
> * break用于跳出当前循环，continue跳出当前迭代;break只能在循环和switch;continue只能在循环中;
> * JS标签：语法： label:statements，需要在代码块前加冒号，而break和continue仅仅只是可以跳出语句break label；通过标签引用，break 语句可用于跳出任何 JavaScript 代码块：
   18. [JavaScript的typeof](http://127.0.0.1:8082/test18)
> * typeof 用于判断值(或对象)的数据类型;
> * null 表示一个空对象应用，undefined代表一个没有设置值的变量，type null 结果是object 而typeof undefined结果是undefined;
> * null == undefined结果是true;null === undefined结果是false;
   19. [JavaScript的类型转换](http://127.0.0.1:8082/test19)
> * 常用的Number(),String(),Boolean();
> * JS中有5中数据类型：string,number,boolean,object,function;3种对象类型：object array Date;2种不包含任何值的数据类型null undefined
> * constructor属性返回变量的构造函数 ,indexOf() 返回的是字符串中首次包含该字符参数的位置
> * JS类型转换：1.变量自身转换；2.通过函数转换；
> * [类型转换相关参考](http://www.runoob.com/js/js-type-conversion.html)
> * JS的一元运算符 +  用于将变量变成数字  var y = '123' ;+ y 结果就是 123；
> * 将布尔值转换为数字  Number(false)  结果是0； Number(true)  结果是1；
   20. [JavaScript的正则表达式](http://127.0.0.1:8082/test20)
> * 常用的search()用于检索子字符串，返回位置,replace()用一些字符替换另外一些字符;
> * var patt=new RegExp(pattern,modifiers); 或者更简单的方式:var patt=/pattern/modifiers;  RegExp 对象是一个预定义了属性和方法的正则表达式对象;其test()用于检测字符串中是否存在匹配模式，返回true/false;exec()用于检索字符串中的正则的模式，返回一个数组，其中存放匹配的结果，没有返回null。
   21. [JavaScript的异常处理](http://127.0.0.1:8082/test21)
> * try 用于检测代码内容 catch 处理错误 throw 创建自定义错误；
> * try {执行代码} catch(err){//异常处理}
> * throw用于自定义错误。
   22. [JavaScript的变量提升](http://127.0.0.1:8082/test22)
> * 这个概念其实是指的是 jS中的函数及变量都会被提升到最顶端，所以变量可以先声明后赋值，也可以先赋值后声明也是可以的；
> * 但需要注意的是： 只有声明的变量会提升，初始化的不会提升；
   23. [JavaScript的严格模式](http://127.0.0.1:8082/test23)
> * JS的“use strict” 用于在全局和函数内部声明严格模式，注意是ECMAScript5新增性能，在之前的版本中出现则无效；
> * 提升安全、效率的合理使用JS;
   24. [JavaScript的常见错误](http://127.0.0.1:8082/test24)
> * 等号判断== 和 = 使用时候的误区：if(=) 如果右侧数值不为0，均为true,否则是false;
> * 在常规的比较中，数据类型是被忽略的,如 if(10 == '10')  结果为true;switch 语句会使用恒等计算符(===)进行比较,也就是严格意义的比较
> * 加号在字符串中和数字中的使用，例如 10+'10' = '1010';
> * JS中的所有数据都是以64位的浮点数据来存储的,所有编程语句，对浮点数的精确度很难确认；
> * 字符串断行需要使用反斜杠(\)，
> * JS允许使用多行来结束一个语句，需要注意的是 如果是一个不完整的语句，JavaScript 将尝试读取第二行的语句；但是对于return 就是结束语句，所有不再读取下一行
> * JS数组不允许使用名字来索引数组，只允许使用数字索引，使用名字来作为索引的数组称为关联数组(哈希)；
> * Undefined 不是 Null,JS中 null 用于对象, undefined 用于变量，属性和方法；对于对象是否存在，先使用 typeof 来检测对象是否已定义；
> * 在每个代码块中 JavaScript 不会创建一个新的作用域，一般各个代码块的作用域都是全局的。
   25.[javascript常常用表单验证](http://127.0.0.1:8082/test25)
> * html表单验证可以通过 JavaScript 来完成;
> * isNaN() 判断是不是数字，是数字为，不是则为false;
> * 表单自动验证(IE9之后的版本)在数据框中添加 required= "required";
> * H5新增了约束验证;
   26.[javascript的json](http://127.0.0.1:8082/test26)
> * json 全称  JavaScript Object Notation,当然也可以用于其他语言中，应用于数据交互和存储等功能上;
> * json 对应于javascript中的对象、数组，逗号分隔，大括号表示对象，方括号表示数组；
> * js中内置函数JSON.parse()用于将字符串转换成json对象；而JSON.stringify()用于将json对象转换成字符串。
   27.[javascript的void](http://127.0.0.1:8082/test27)
> * void是执行内部的表达式，但是没有返回值的关键字；
> * href="#"与href="javascript:void(0)"的区别:1.# 包含了一个位置信息，默认的锚是#top 也就是网页的上端。而javascript:void(0), 仅仅表示一个无效链接。在页面很长的时候会使用 # 来定位页面的具体位置，格式为：# + id。



















