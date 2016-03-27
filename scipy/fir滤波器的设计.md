#FIR滤波器的设计
**在数字信号处理领域，数字滤波器占有非常重要的地位，根据其计算方式可以分为FIR(有限脉冲响应)滤波器和IIR(无限脉冲响应)滤波器两种。FIR滤波器在某一时刻的输出只与这一时刻及之前的输入有关，而IIR滤波器某一时刻的输出不仅与这一时刻及之前的输入有关，还与这一时刻之前的输出有关。**
##低通滤波器的设计
**根据理想低通滤波器的脉冲响应公式设计：**   
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/ideal.png)
###代码
<pre>
# -*- coding: utf-8 -*-
import pylab as pl
import scipy.signal as signal
import numpy as np

sampling_rate = 2000
# 低通FIR滤波器的设计
def h_ideal(n,fc):
    return 2*fc*np.sinc(2*fc*np.arange(-n,n,1.0))

b = h_ideal(1000,0.25)
w, h = signal.freqz(b)
power = 20*np.log10(np.clip(np,abs(h),1e-8,1e100))#幅度响应
phase = np.arctan(h.imag/h.real)/np.pi*180#相位响应

pl.plot(w/np.pi/2*sampling_rate,power,label='n=1000')
pl.xlabel('Hz')
pl.ylabel('Gain(dB)')
pl.legend()
pl.show()
</pre>
###结果
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/LPF-1.png)
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/LPF-2.png)
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/LPF-3.png)
###小结
**显然，根据理想低通滤波器的脉冲响应公式设计的低通滤波器随着n的增大越来越接近理想，但是这样做给系统增加了延时；为了频率响应更好必须增加滤波器的点数，然而为了减少延时，必须减少点数，为了解决这个矛盾，scipy的signal库中提供了firwin函数，给系数乘上一个窗函数，让它快速收敛。**   
****
**用firwin函数设计：**
<pre>
# -*- coding: utf-8 -*-
import pylab as pl
import scipy.signal as signal
import numpy as np

sampling_rate = 2000
# 低通FIR滤波器的设计
def h_ideal(n,fc):
    return 2* fc * np.sinc(2* fc *np.arange(-n,n,1.0))

b1 = h_ideal(300,0.25)
w1, h1 = signal.freqz(b1)
power1 = 20 * np.log10(np.clip(np,abs(h1),1e-8,1e100))#幅度响应
phase1 = np.arctan(h1.imag/h1.real)/np.pi*180#相位响应

b2 = signal.firwin(len(b1),0.5)
w2, h2 = signal.freqz(b2)
power2 = 20 * np.log10(np.clip(np,abs(h2),1e-8,1e100))#幅度响应
phase2 = np.arctan(h2.imag/h2.real)/np.pi*180#相位响应

pl.plot(w1/np.pi/2 * sampling_rate,power1,label=u'h_ideal')
pl.plot(w1/np.pi/2*sampling_rate,power2,label=u'firwin')
pl.xlabel('Hz')
pl.ylabel('Gain(dB)')
pl.legend()
pl.show()
</pre>
###结果
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/LPF-4.png)
###小结
**在相同的点数的情况下，firwin函数能够达到更好的效果，但是这并不是最优化的，为了实现同样效果的频率响应，还存在更短的FIR滤波器。**
****
**用remez函数设计：**
<pre>
# remez函数的调用格式
remez(numtaps, bands, desired, weight=None, Hz=1, type='bandpass', maxiter=25, grid_density=16)
# numtaps: 所设计的FIR滤波器的长度
# bands：一个递增序列，它包括频率响应中的所有频带的边界，其值在0到Hz/2之间
# desired: 长度为bands的一半的增益序列，它给出频率响应在bands中的每个频带的增益值，由它来控制滤波器的类型
# weight: 长度和desired一样的权重序列，它给出的desired中的每个增益所占的比重
</pre>
###代码
<pre>
import pylab as pl
import scipy.signal as signal
import numpy as np

sampling_rate = 2000

# 给定设计指标
wp = 0.2 * np.pi
ws = 0.3 * np.pi
Rp = 0.25
As = 50.0

delta1 = (10**(Rp/20)-1)/(10**(Rp/20)+1)# 求通带的绝对波动指标
delta2 = (1+delta1)*(10**(-As/20))# 求阻带绝对波动指标
weights = np.array([delta2/delta1, 1.0])# remez要求的加权向量
deltaf = (ws-wp)/(2*np.pi)# 估算N需要的过渡带宽度
N = np.ceil((-20*np.log10(np.sqrt(delta1*delta2))-13)/(14.6*deltaf)+1)# 估算N
N = np.int(N+np.mod(N-1,2))# N必须为奇数
f = np.array([0.0, wp/np.pi, ws/np.pi, 0.5])# 函数要求的频率向量
m = np.array([1.0,0.01])# remez函数要求的理想幅频特性向量

b = signal.remez(N, f, m, weights)
w, h = signal.freqz(b,1)
power = 20*np.log10(np.clip(np.abs(h),1e-20,1e100))


pl.plot(w/np.pi/2*sampling_rate,power)
pl.xlabel('Hz')
pl.ylabel('Gain(dB)')
pl.show()
</pre>
###结果
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/LPF-5.png)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                             Stay hungry, Stay foolish. ---Steve Jobs
