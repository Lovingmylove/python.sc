#scipy库中插值运算及其应用
**scipy.interpolate对从实验数据拟合函数来求没有测量点的值非常有用**
##线性插值与B-Spline插值
###代码
<pre>
# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from scipy import interpolate

x = np.linspace(0,2*np.pi+np.pi/4,10)
y = np.sin(x)

x_new = np.linspace(0,2*np.pi+np.pi/4,100)
f_linear = interpolate.interp1d(x,y)
tck = interpolate.splrep(x,y)
y_bspline = interpolate.splev(x_new,tck)

pl.plot(x,y,'ro',label='original data')
pl.plot(x_new,f_linear(x_new),'*',label='linear interpolation')
pl.legend()
pl.figure()
pl.plot(x,y,'ro',label='original data')
pl.plot(x_new,y_bspline,'.',label='B-spline interpolation')
pl.legend()
pl.show()
</pre>
###插值结果
![linear interpolation](/Users/Lovingmylove521/Desktop/scipy/linear_interpolation.png)
![B-Spline](/Users/Lovingmylove521/Desktop/scipy/B-Spline_interpolation.png)
###小结
**B-Spline插值显然比线性插值的效果好，但是两者都只能预测自变量范围之内的点，而不能预测超出自变量范围的点。**
##U-Spline插值
###代码
<pre>
import numpy as np
from scipy.interpolate import UnivariateSpline
import pylab as pl

x = np.linspace(0,2*np.pi,10)
y = np.sin(x)

y_spline = UnivariateSpline(x, y)
x_new = np.linspace(0,2*np.pi,100)

x_dot = np.linspace(2*np.pi,2*np.pi+0.5,10)
y_dot = y_spline(x_dot)

pl.plot(x,y,'ro',label='original data')
pl.plot(x_new,y_spline(x_new),'g--',label='U-Spline')
pl.plot(x_dot,y_dot,'*',label='prediction data')
pl.plot(x_dot,np.sin(x_dot),'.')
pl.legend()
pl.show()
</pre>
###插值结果
![U-Spline](/Users/Lovingmylove521/Desktop/scipy/U-Spline.png)
###小结
**U-Spline插值虽然可以预测自变量范围之外的数据，但是其预测精度随着偏离范围的增大而增大。**
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                       Stay hungry, Stay foolish. ---Steve Jobs
