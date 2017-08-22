# tech_web notes
### tutorial section01:javascript ##
   1. [JavaScript动态效果初体验](http://127.0.0.1:8082/test01)
   2. [JavaScript的初步介绍](http://127.0.0.1:8082/test02)
* html输出流写法document.write()及其页面加载后的区别;
* js执行动作效果;
* js获得元素document.getElementByXX以及修改元素信息
   3. [JavaScript的使用](http://127.0.0.1:8082/test03)
* js代码涉及script标签的位置；
* 引用外部js库的方式
   4. [JavaScript的输出](http://127.0.0.1:8082/test04)
* 方式1:window.alert('infos')弹出警告框；
* 方式2:document.write('infos')将内容写到html文档中
* 方式3:通过innerHTML写入到Html元素中
* 方式4:通过console.log()写入到浏览器的控制台
    > 说明1：console调试相比较于alert()方式优越：其一不影响页面调试；其二可以显示更详细的结构信息；
            document.write()是直接入到入到html页面中的，期间浏览器会自动调用documnet.open(),所以每次关闭write之后，页面会被重写；
            而innerHTML是Dom页面元素的一个属性，代表元素精确的内容，写法是：document.(getElementByXX).innerHTML。

    > 说明2：提及DOM:DOM(documnet object model)即文档对象模型，DOM是将文档描述成是一个树型结构。


