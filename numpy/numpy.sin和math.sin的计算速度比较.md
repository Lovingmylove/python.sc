#numpy.sin和math.sin的计算速度比较
![sin](https://github.com/Lovingmylove/python.sc/blob/master/numpy/sin.gif "github")
##代码
<pre>
import time				
import math	 							
import numpy as np			
x=[i*0.001 for i in xrange(1000000)]  
start=time.clock()		
for i,t in enumerate(x):	
    x[i]=math.sin(t)		
print "math.sin:",time.clock()-start 
x=[i*0.001 for i in xrange(1000000)]  
x=np.array(x)  
start=time.clock()  
np.sin(x,x)  
print "numpy.sin:",time.clock()-start
</pre>
##运行结果
<pre>
#输出
math.sin: 0.352168
numpy.sin: 0.015086
</pre>
**在我的电脑上计算100万次正弦值，numpy.sin比math.sin快20倍多，这得力于numpy.sin在c语言级别的循环计算。**
***
**同样，numpy.sin同样支持对单个数值求正弦，不过，对单个数的计算math.sin则比numpy.sin快很多。**
##代码
<pre>
x=[i*0.001 for i in xrange(1000000)]
start=time.clock()
for i,t in enumerate(x):
    x[i]=np.sin(t)
print "numpy.sin loop:",time.clock()-start
</pre>
##运行结果
<pre>
#输出
numpy.sin loop: 1.082252
</pre>
**numpy.sin的计算速度只有math.sin的1/3，这是因为numpy.sin为了同时支持数组和单个数值的计算，其C语言的内部实现要比math.sin复杂的多，如果我们同样在python级别进行循环的话，就会看出其中的差别。**
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                     Stay hungry, Stay foolish. ---Steve Jobs
