#Extremum algorithm
**< 1. > 极值是一个函数的极大值或极小值。如果一个函数在一点的一个邻域内处处都有确定的值，而以该点处的值为最大（小），这函数在该点处的值就是一个极大（小）值。如果它比邻域内其他各点处的函数值都大（小），它就是一个严格极大（小）。该点就相应地称为一个极值点或严格极值点。**   
**< 2. > 函数的一种稳定值，即一个极大值或一个极小值，极值点只能在函数不可导的点或导数为零的点上取得。**
![extremum](/Users/Lovingmylove521/Desktop/python.sc/project/OEO/extremum.png)    
***#图中B,C,D,E是极值点***
##程序
<pre>
# -*- coding: utf-8 -*-
import numpy as np


#测试数据
a = [1,2,3,4,5,6,5,4,6,8,10,5,5,5,5,5,4,4,5,5,6,7,7,7,7,7,7,4]


# 定义寻极值函数，选择返回极大值和极小值
def extremum(a):
    maxima = []
    minima = []
    for i in np.arange(1,len(a)-1):
        if (a[i-1] < a[i] and a[i+1] <= a[i]):
            maxima.append(a[i])   
        elif (a[i-1] > a[i] and a[i+1] >= a[i]):
            minima.append(a[i])
    if (len(maxima)==0):
        maxima.append(np.max(a))
    if (len(minima)==0):
        minima.append(np.min(a))
    return maxima, minima
    
print extremum(a)[0][0]
</pre>
**判断条件中“=”的选取与否，决定了输出的是严格的极值点还是非严格的极值点。**
##输出结果
<pre>
>> ([6, 10, 5, 7], [4, 5, 4])
</pre>
**输出的结果是一个tuple，对tuple元素的访问如下所示：**
<pre>
extremum(a)[0]#输出所有的maxima
extremum(a)[1]#输出所有的minima
extremum(a)[0][m]#输出第m+1个maxima
extremum(a)[1][n]#输出第n+1个minima
</pre>
**例如：extremum(a)[0][0]**
<pre>
>> 6 #maxima中的第1个
</pre>
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                        Stay hungry, Stay foolish. ---Steve Jobs