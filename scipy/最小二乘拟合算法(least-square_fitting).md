#最小二乘拟合算法(Least-square fitting)
   ![Least-square fitting](https://github.com/Lovingmylove/python.sc/raw/master/scipy/least_square.gif)  
**最小二乘拟合算法适用于这样的场景：已知一组实验数据(x[i],y[i]),也知道它们之间的函数关系y=f(x)，需要确定函数中的一些参数项。**  
**高斯函数在数学，自然科学以及工程学领域都是很常用的函数，用最小二乘拟合算法进行高斯拟合是常用的一种方法。**
##代码
<pre>
# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
def func(x,p):
    a,b,c = p
    return a*np.exp(-(x-b)**2/(2*c**2))
def residuals(p,y,x):
    return y - func(x,p)

x=np.linspace(-5,5,100)
a,b,c = 10,0,0.5
y0 = func(x,[a,b,c])
y1 = y0+0.5*np.random.normal(0,0.5,len(x))

p0 = [8,0.2,0.2]
plsq = leastsq(residuals,p0,args=(y1,x))

print u"真实参数:" , [a,b,c]
print u"拟合参数:" , plsq[0]

#pl.plot(x,y0,'r',label='Ture data')
pl.plot(x,y1,'b-.',label='Data with noise')
pl.plot(x,func(x,plsq[0]),'y-*',label='Fitting data')

pl.legend()
pl.show()
</pre>
##运行结果
<pre>
#输出
真实参数: [10, 0, 0.5]
拟合参数: [  1.01505760e+01  -2.05324950e-03   5.19273958e-01]
</pre>
##拟合结果
![Gaussian_Function_Fitting](https://github.com/Lovingmylove/python.sc/raw/master/scipy/Gaussian_Function_Fitting.png)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                    Stay hungry, Stay foolish. ---Steve Jobs
