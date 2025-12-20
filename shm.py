import matplotlib.pyplot as plt
import numpy as np
xi=0
yi=4
xf=100
zi=0
n=10001
mi=-9*yi
h=(xf-xi)/(n-1)
xx=[]
yy=[]
xx.append(xi)
yy.append(yi)
for i in range(1,n):
    x=xi+i*h
    zf=zi+h*mi
    yf=yi+h*zi
    mf=-9*yf
    zi=zf
    mi=mf
    yi=yf
    xx.append(x)
    yy.append(yf)
plt.plot(xx,yy,'-r')
plt.grid()
plt.show()
plt.show()