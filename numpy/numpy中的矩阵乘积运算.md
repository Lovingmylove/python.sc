#numpy中的矩阵乘积运算
![array](/Users/Lovingmylove521/Desktop/numpy/array.jpeg)
##简介
**numpy提供了dot,inner,outer等多种矩阵乘积的函数，这些函数计算乘积方式不同，尤其是多维数组，更容易搞混。**
##dot
**对于两个一维数组，计算的是这两个数组对应下标的乘积和（内积）；对于二维数组，计算的是两个数组的矩阵乘积；对于多维数组，它的计算公式如下所示，其要保证数组a的最后一维和数组b的倒数第二维长度相同。**
<pre>
dot(a,b)[i,j,k,m] = sum(a[i,j,:] * b[k,:m])
</pre>
##inner
**和dot乘积一样，对于两个一维数组，计算的是这两个数组对应下标元素的乘积和；对于多维数组，它计算的结果数组中的每个元素都是：数组a和b最后一维的内积，因此，数组a和b的最后一维的长度必须相同。**
<pre>
inner(a,b)[i,j,k,m] = sum(a[i,j,:],b[k,m,:])
</pre>
##outer
**和dot与inner不一样，outer只按一维数组进行计算，如果传入参数是多维数组，则先将此数组展平为一维数组之后再计算。**
##一维矩阵乘积
###代码
<pre>
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.dot(a.reshape(-1,1),b.reshape(1,-1))
d = np.inner(a.reshape(-1,1),b.reshape(-1,1))
</pre>
###运行结果
<pre>
>>>c == d
array([[ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True]], dtype=bool)
</pre>
##二维矩阵乘积
###代码
<pre>
import numpy as np
e = np.linspace(1,10,10).reshape(5,2)
f = np.arange(3,5)
g = np.dot(e,f.reshape(-1,1))
h = np.inner(e,f.reshape(1,-1))
</pre>
###运行结果
<pre>
>>>g == h
array([[ True],
       [ True],
       [ True],
       [ True],
       [ True]], dtype=bool)
</pre>
##小结
**从上面的一维和二维矩阵我们可以看到，dot跟我们平时的矩阵乘积运算习惯一致，inner函数则不一致，不过两者可以得到相同的运算结果。**
##应用：求解多元一次方程组
###代码
<pre>
import numpy as np
a = np.random.rand(20,20)
b = np.random.rand(20)
x = np.linalg.solve(a,b)
error =np.sum(np.abs(np.dot(a,x)-b))
</pre>
###运算结果
<pre>
>>>error
5.2180482157382357e-15
</pre>
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                      Stay hungry, Stay foolish. ---Steve Jobs