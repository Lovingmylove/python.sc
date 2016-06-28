#Bessel functions in scipy
***The scipy.special module including a large number of bessel-functions. Here we will use the function jn and yn, which are the Bessel functions of the first and second kind and real-valued order. We also include the function jn_zeros and yn_zeros that gives the zeros of the function jn and yn.***
##Bessel function and Bessel-cardinal function
<pre>
# Bessle function 的调用方式
from scipy.special import jn, yn, jn_zeros, yn_zeros
</pre>
**注：**   
**jn: Bessel function of first order**   
**yn: Bessel function of second order**   
**jn_zeros: zeros of Bessel function of first order**   
**yn_zeros: zeros of Bessel function of first order**  
<pre>
# -*- coding: utf-8 -*-
from scipy.special import jn
import pylab as pl
import numpy as np


#自变量及第一类贝塞尔函数阶数设置
x = np.linspace(0.00000001,100,10000)
n = 1

#besselcardinal函数
def besselcardinal(n,x):
    return jn(n,x)/x

#绘图
m = np.max(besselcardinal(n,x))
pl.plot(x,besselcardinal(n,x),label='Bessel-cardinal function (n=1)',linewidth=1)
pl.plot(x,jn(n,x),'g',label='Bessel Function (n=1)',linewidth=1)
pl.plot(0,m,'ro',linewidth=2)
pl.legend()
pl.title(u'Bessel-cardinal Function compared to Bessel Function')
pl.text(2.5,0.487,' <--- maximum=%0.2f' %(m))#在图中插入文本信息
pl.show()
</pre> 
##结果
![Bessel-cardinal function](https://github.com/Lovingmylove/python.sc/raw/master/project/OEO/Besselfunction.png) 
**从Bessel-cardinal function 和 Bessel function 的对比图中可以看出，在零点附近，Bessel-cardinal function 有 maximum=0.50**
##zeros of Bessel function
<pre>
print jn_zeros(n,m)
#n: the order of the first kind Bessel function; 
#m: number of roots to compute
</pre>
**以n=1，m=10为例**
##结果
<pre>
[  3.83170597   7.01558667  10.17346814  13.32369194  16.47063005
  19.61585851  22.76008438  25.90367209  29.04682853  32.18967991]
</pre>
### More special function in Scipy
[Scipy.special](http://docs.scipy.org/doc/scipy/reference/special.html#module-scipy.special)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                        Stay hungry, Stay foolish. ---Steve Jobs
