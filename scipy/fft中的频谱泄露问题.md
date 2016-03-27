#FFT中的频谱泄露问题
**将时域信号通过FFT转换为频域信号之后，将其各个频率分量的幅值绘制成图，可以很直观地观察信号的频谱。但，往往因为我们设置参数的问题，导致我们得到的频谱有别于实际情况。**
##代码
<pre>
import numpy as np
import pylab as pl

sampling_rate = 8000
fft_size = 512
t = np.arange(0,1.0,1.0/sampling_rate)
x = np.sin(2*np.pi*156.25*t) + 2*np.sin(2*np.pi*234.375*t)
xs = x[:fft_size]
xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0,sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf),1e-20,1e100))

pl.figure(figsize=(8,5))
pl.subplot(211)
pl.plot(t[:fft_size],xs)
pl.xlabel("Time(s)")
pl.title("156.25Hz and 234.375Hz's wave and spectrum")
pl.subplot(212)
pl.plot(freqs,xfp)
pl.xlabel("Hz")
pl.subplots_adjust(hspace=0.4)
pl.show()
</pre>
##FFT频谱
![fft-1](https://github.com/Lovingmylove/python.sc/raw/master/scipy/fft-1.png)
###为什么是“156.25Hz”和“234.375Hz”这两个奇怪的频率？
**因为在我们设置的条件下，这两个频率的正弦波在512个取样点中正好有整数个周期，满足这个条件波形的FFT结果能够精确地反应其频谱。**
![fft-2](https://github.com/Lovingmylove/python.sc/raw/master/scipy/fft-2.png)      
**把频率换成200Hz和300Hz，得到的不再是两个完美的峰值，而是两个峰值频率周围的频率都有能量，这种现象被称为频谱泄露。原因在于fft_size个取样点无法放下整数个200Hz和300Hz的波形。**
<pre>
sampling_rate = 5120
</pre>      
**把采样频率改为5.12kHz,这样5120/512=10Hz,200Hz和300Hz都是10的整数倍，就能画出完美的频谱图。**
![fft-3](https://github.com/Lovingmylove/python.sc/raw/master/scipy/fft-3.png)
##频谱泄露解释
<pre>
t = np.arange(0,1.0,1.0/4000)
x = np.sin(2*np.pi*200*t)[:128]
pl.plot(np.hstack([x,x,x]))
pl.xlabel("sampling")
pl.title(u"200Hz sine wave")
pl.show()
</pre>
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/fft-4.png)      
**波形前后不连续，出现跳变，而跳变处有着非常广泛的频率，因此FFT结果中出现频谱泄露。**
##利用hann窗函数减少FFT所取截断数据的跳变
<pre>
import numpy as np
import pylab as pl
import scipy.signal as signal

sampling_rate = 8000
fft_size = 512
t = np.arange(0,1.0,1.0/sampling_rate)
x = np.sin(2*np.pi*200*t)+2*np.sin(2*np.pi*300*t)

xs = x[:fft_size]
ys = 2*xs*signal.hann(fft_size,sym=0)

xf = np.fft.rfft(xs)/fft_size
yf = np.fft.rfft(ys)/fft_size
freqs = np.linspace(0,sampling_rate/2,fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf),1e-20,1e100))
yfp = 20*np.log10(np.clip(np.abs(yf),1e-20,1e100))

pl.figure(figsize=(8,5))
pl.title("200Hz and 300Hz's wave and spectrum")
pl.plot(freqs, xfp,label='With rectangle window')
pl.plot(freqs, yfp,label='With hann window')
pl.legend()
pl.xlabel("Hz")

a = pl.axes([.4,.2,.4,.4])
a.plot(freqs,xfp,label="with rectangle window")
a.plot(freqs,yfp,label="with hann window")
a.set_xlim(100,400)
a.set_ylim(-40,0)
pl.show()
</pre>
###结果
![hann](https://github.com/Lovingmylove/python.sc/raw/master/scipy/hann.png)      
**加上hann窗口后，FFT截断的数据中跳变就会减少，进而使得能量更加集中，加上hann窗口后的FFT采样图像如下所示：**
![](https://github.com/Lovingmylove/python.sc/raw/master/scipy/hann-1.png)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                        Stay hungry, Stay foolish. ---Steve Jobs
