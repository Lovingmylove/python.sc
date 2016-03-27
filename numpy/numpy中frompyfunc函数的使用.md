#numpy中frompyfunc函数的使用
**通过组合标准的ufunc函数的调用，可以实现各种算式的数组计算，不过有些时候这种算式不易编写，而针对每个元素的计算函数却很容易用Python实现，这时可以用frompyfunc函数将一个计算单个元素的函数转换成ufunc函数，从而很大程度上提高效率。**
![triangle_wave](https://github.com/Lovingmylove/python.sc/raw/master/numpy/triangle_wave.png)
##代码（Python）
<pre>
import numpy as np
import time
def triangle_wave(x,c,c0,hc):
    x=x-int(x)
    if x < c:
        r=0.0
    elif x < c0:
        r=x/c0*hc
    else:
        r=(c-x)/(c-c0)*hc
    return r
x=np.linspace(0,2,1000000)
start=time.clock()
y=np.array([triangle_wave(t,0.6,0.4,1.0) for t in x])
</pre>
##运行结果
<pre>
#输出
triangle_wave: 1.06266
</pre>
**显然，triangle_wave函数只能计算单个数值，不能对数组直接处理。可以用上述列表包容，计算出一个list，然后用array函数将列表转换为数组，运行100万次的时间在1秒左右，显然效率是不高的。**
##代码（frompyfunc）
<pre>
import numpy as np
import time
def triangle_wave(x,c,c0,hc):
    x=x-int(x)
    if x < c:
        r=0.0
    elif x < c0:
        r=x/c0*hc
    else:
        r=(c-x)/(c-c0)*hc
    return r
triangle_ufunc=np.frompyfunc(lambda x: triangle_wave(x,0.6,0.4,1.0),1,1)
y=triangle_ufunc(x)
print "triangle_ufunc:", time.clock()-start
</pre>
##运行结果
<pre>
#输出
triangle_ufunc: 0.672269
</pre>
**利用frompyfunc生成triabgle_ufunc函数对数组进行计算显然提高了效率，但是triangle_wave函数的4个参数中只有x是不确定的，因此所产生的ufunc函数其实只有一个参数，为了满足这个条件，我们利用lambda对triangle_wave函数的参数进行包装，但是这样做，效率依然不高。**
##代码（改进的frompyfunc）
<pre>
import numpy as np
import time
def triangle_func(c,c0,hc):
    def trifunc(x):
        x=x-int(x)
        if x < c:
            r=0.0
        elif x < c0:
            r=x/c0*hc
        else:
            r=(c-x)/(c-c0)*hc
        return r
    return np.frompyfunc(trifunc,1,1)
x=np.linspace(0,2,1000000)
start=time.clock()
y=triangle_func(0.6,0.4,1.0)(x)
print "triangle_func:", time.clock()-start
</pre>
##运行结果
<pre>
#输出
triangle_func: 0.56715
</pre>
**通过triangle_func函数包装三角波的三个参数，在其内部定义一个计算三角波的函数trifunc，trifunc函数调用时会采用triangle_func的参数计算，最后triangle_func返回用frompyfunc转换结果。**
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                     Stay hungry, Stay foolish. ---Steve Jobs
