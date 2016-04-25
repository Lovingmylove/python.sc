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
# 任意偏移的三角函数函数
def triangle_wave(arr_x,p):
    a,T = p
    y = np.where(np.mod(arr_x-a,T)<T/2, -4/T*(np.mod(arr_x-a,T))+1, 0)
    y = np.where(np.mod(arr_x-a,T)>=T/2, 4/T*(np.mod(arr_x-a,T))-3, y)
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