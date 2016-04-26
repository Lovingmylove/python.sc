#任意波形的RMSE(root-mean-square error)计算
**均方根误差，它是观测值与真值偏差的平方和观测次数n比值的平方根，在实际测量中，观测次数n总是有限的，真值只能用最可信赖（最佳）值来代替.方根误差对一组测量中的特大或特小误差反映非常敏感，所以，均方根误差能够很好地反映出测量的精密度。**   
![RMSE](https://github.com/Lovingmylove/python.sc/raw/master/project/RMSE/RMSE.png)   
**观测值一般为我们实验中获取的数据，真值通常是通过对观测数据进行对应函数拟合得到的，那么什么样的拟合方式才是最适合的呢？**
##最小二乘拟合函数
scipy库中提供了最小二乘拟合的算法：leastsq，其调用方式为：
<pre>
from scipy.optimize import leastsq
</pre>
##以三角函数的RMSE计算为例，那么任意形式的三角波如何生成？
<pre>
def triangle_wave(arr_x,p):
    a,T = p
    y = np.where(np.mod(arr_x-a,T) < T/2, -4/T* (np.mod(arr_x-a,T))+1, 0)
    y = np.where(np.mod(arr_x-a,T) >= T/2, 4/T* (np.mod(arr_x-a,T))-3, y)
    return y
</pre>
入参为自变量arr_x, 时延a, 周期T,这三个参数决定了一个任意形式的三角波。实验数据：f = 4 GHz，时延不确定的三角波；
##程序
<pre>
# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from scipy.optimize import leastsq

#数据的读取
#横坐标数据
flagx = 0
flagy = 0
flagend = 16200
fx = open(r"/Users/Lovingmylove521/Desktop/python.sc/project/RMSE/datax.txt","r")
arrx=[] 
for lines in fx.readlines(): 
    lines=lines.replace("\n","").split(" ") 
    arrx.append(lines)
    flagx += 1
    if flagx > flagend:
        break  
fx.close()
#纵坐标数据
fy = open(r"/Users/Lovingmylove521/Desktop/python.sc/project/RMSE/datay.txt","r")
arry=[] 
for lines in fy.readlines(): 
    lines=lines.replace("\n","").split(" ") 
    arry.append(lines)
    flagy += 1
    if flagy > flagend:
        break  
fy.close()
#数据形式的转换
arr_x =[]
for i in np.arange(0,len(arrx)):
    arr_x.append(float(arrx[i][0])/1e12)

arr_y =[]
for i in np.arange(0,len(arry)):
    arr_y.append(float(arry[i][0]))
# 任意偏移的三角波函数
def triangle_wave(arr_x,p):
    a,T = p
    y = np.where(np.mod(arr_x-a,T) < T/2, -4/T*(np.mod(arr_x-a,T))+1, 0)
    y = np.where(np.mod(arr_x-a,T) >= T/2, 4/T*(np.mod(arr_x-a,T))-3, y)
    return y

# 误差函数
def residuals(p,y,x):
    return y - triangle_wave(arr_x,p)
    
# 待拟合数据
#x = np.arange(0,0.4,0.0001)
#y0 = triangle_wave(x,[0.03,0.1])
#y1 = y0 + 0.01*np.random.normal(0,0.5,len(x))

# 拟合方程
p0 = [215e-12,2.50e-10]
plsq = leastsq(residuals,p0,args=(arr_y,arr_x))
y2 = triangle_wave(arr_x,plsq[0])

# 画图
#pl.plot(x,y1,'r-.',label='Data with noise')
pl.plot(arr_x,y2,'r-',label='Fitting data',linewidth=3)
pl.plot(arr_x,arr_y,label='Experiment data',linewidth=1)
pl.legend()
pl.show()

# 计算RMSE
variance = 0
for t in np.arange(0,len(arr_x),len(arr_x)):
    variance += (arr_y[t]-y2[t])**2
    
RMSE =  np.sqrt(variance/len(arr_x))
print RMSE,plsq[0]
</pre>
##结果
<pre>
0.000644029630755 [  2.15530437e-10   2.51348298e-10]
</pre>
均方根误差：RMSE = ~6.4e-4   
时延：a = ~2.16e-10   
周期：T = ~2.51e-10
![RMSE](https://github.com/Lovingmylove/python.sc/raw/master/project/RMSE/triangular.png)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                        Stay hungry, Stay foolish. ---Steve Jobs
