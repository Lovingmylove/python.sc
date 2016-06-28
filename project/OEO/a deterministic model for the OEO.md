# A deterministic model for the OEO
**We have drived a first-order nonlinear delay-differential equation with a complex variable to investigate the dynamic of the OEO.**   
![FONDDE](https://github.com/Lovingmylove/python.sc/raw/master/project/OEO/FONDDE.gif)   
**注释：**   
<pre>
u: the half-bandwidth of electrical bandpass filter
y: the effective feedback gain
segam: the cumulated loop phase
Jc1: the Bessel-cardinal function
A: the amplitude of the oscillating microwave signal
At: the time-delay microwave signal of A
</pre>
##程序
<pre>
# -*- coding: utf-8 -*-
import numpy as np
import sys
sys.path.append(r'/Users/Lovingmylove521/Downloads')
from besselcardinal import besselcardinal
import pylab as pl


#矩阵初始化
amplitude = np.zeros(10000)+1e-2


#微分方程参数设置
u = 0.06
y = -2.55
e = 0


#求解
t = np.arange(200,10000)
for i in t:
    amplitude[i] = 2*(-u*amplitude[i-1]-2*u*y*besselcardinal(1,2*np.abs(amplitude[i-t[0]]))*amplitude[i-t[0]])+amplitude[i-1]
  
#数据类型的转换
a =[]
for i in t:
    a.append(float(i)/t[0])

#数据可视化
pl.plot(a,amplitude[t])
pl.show()
</pre>
##输出结果
![y=-2.2](https://github.com/Lovingmylove/python.sc/raw/master/project/OEO/y=-2.2.png)
![y=-2.4](https://github.com/Lovingmylove/python.sc/raw/master/project/OEO/y=-2.4.png)
##总结
**Numerical simulation of the deterministic model of OEO for various of the effective feedback gain. When |y|=2.2 < ycr, the system converges to stable fixed point after some oscillatory transients. When |y| = 2.4 > ycr, the system is beyond the supercritical Hopf bifurcation value, and its amplitude is mudulated with a period equal to 2T.**
##Stationary solutions and their stability
###程序
<pre>
# -*- coding: utf-8 -*-
import numpy as np
import sys
sys.path.append(r'/Users/Lovingmylove521/Downloads')
from besselcardinal import besselcardinal
from extremum import extremum
import pylab as pl


#矩阵初始化
amplitude = np.zeros(20000)+1e-2


#微分方程参数设置
u = 0.06
y_lin = np.linspace(-0.01,-2.6,260)
absy = np.abs(y_lin)
#y = -2.28
e = 0
extremum_list_max = []
extremum_list_min = []

#求解
for y in y_lin:
    t = np.arange(200,20000)
    for i in t:
        amplitude[i] = 2*(-u*amplitude[i-1]-2*u*y*besselcardinal(1,2*np.abs(amplitude[i-t[0]]))*amplitude[i-t[0]])+amplitude[i-1]
    extremum_list_max.append(extremum(amplitude[19950:20000])[0])
    extremum_list_min.append(np.min(amplitude[19800:20000]))
    if np.max(amplitude[19950:20000]) - np.min(amplitude[19800:20000]) >= 0.01:
        print y #输出y用于观测Neimark-Sacker Bifurcation 
  
#数据可视化
pl.plot(absy,extremum_list_max,'r.')
pl.plot(absy,extremum_list_min,'r.')
pl.text(1.05,0,'Hopf Bifurcation \nat |y|=1')
pl.text(1.7,0.8,'Neimark-sacker Bifurcation \nat |y|=2.31')
pl.ylim(-0.2,1.6)
pl.show()
</pre>
###输出结果
![Hopf](https://github.com/Lovingmylove/python.sc/raw/master/project/OEO/hopf.png)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                        Stay hungry, Stay foolish. ---Steve Jobs
