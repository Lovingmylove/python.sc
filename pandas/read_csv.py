# -*- coding: utf-8 -*-
import csv
import numpy as np
import pylab as pl

csvfile = file('/Users/Lovingmylove521/Downloads/example.csv', 'rb')
reader = csv.reader(csvfile)

datax=[]
datay=[]
for line in reader:
    datax.append(line[0])
    datay.append(line[1])
    
x=[]
y=[]
for i in np.arange(43,len(datax)):
    x.append(float(datax[i])/1e9)
    y.append(float(datay[i]))
    
sort_y=[]
sort_y=sorted(y)

pl.plot(x,y,'r')
pl.xlim(0.01,10)
pl.ylim(-70,0)
pl.xlabel('GHz')
pl.ylabel('dBm')
pl.title('2.5GHz triangular pulses spectrum')
pl.text(2.5,sort_y[len(y)-1], sort_y[len(y)-1])
pl.text(5.0,sort_y[len(y)-4], sort_y[len(y)-4])
pl.text(7.5,sort_y[len(y)-2], sort_y[len(y)-2])
pl.show()
