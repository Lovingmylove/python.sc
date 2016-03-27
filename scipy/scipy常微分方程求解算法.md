#常微分方程求解算法
**scipy.integrate提供了数值积分和常微分方程组求解算法odeint,其类似于Matlab中的ode函数，下面就来演示一下odeint计算洛伦兹吸引子的轨迹。**
##代码
<pre>
# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import numpy as np

def lorenz(w,t,p,r,b):
    x,y,z = w
    return np.array([p*(y-x),x*(r-z)-y,x*y-b*z])

t = np.arange(0,30,0.01)#设置时间范围
track1 = odeint(lorenz, (0.0,1.00,0.0), t , args=(10.0, 28.0, 3.0))
track2 = odeint(lorenz, (0.0,1.01,0.0), t , args=(10.0, 28.0, 3.0))#不同初值

#绘图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track1[:,0],track1[:,1],track1[:,2],'r')
ax.plot(track2[:,0],track2[:,1],track2[:,2],'b')
plt.show()
</pre>
##绘图
![Lorenz](https://github.com/Lovingmylove/python.sc/raw/master/scipy/Lorenz.png)
##插曲
**最初在使用Canopy时，命令行“from mpl_toolkits.mplot3D import Axes3D”出现没有功能模块的错误无法调用，于是就用如下的命令查看了一下是否存在该库：**
<pre>
import importlib
importlib.import_module('mpl_toolkits').__path__
</pre>
**该命令行会返回所查库的地址，在我的电脑上返回的地址如下所示：**
<pre>
['/Users/Lovingmylove521/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages/mpl_toolkits']
</pre>
**按照这个路径就能找到相应的库，修改初始化文件即可。**
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                       Stay hungry, Stay foolish. ---Steve Jobs
