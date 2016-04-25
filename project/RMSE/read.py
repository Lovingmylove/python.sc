import numpy as np
f = open(r"C:\Users\tudan\Desktop\example\datax.txt","r")
arrx=[] 
flag = 0
for lines in f.readlines(): 
    lines=lines.replace("\n","").split(" ") 
    arrx.append(lines)
    flag += 1
    if flag > 3000:
        break 
f.close()
arr_x =[]
for i in np.arange(0,len(arrx)):
    arr_x.append(float(arrx[i][0]))
print len(arr_x)