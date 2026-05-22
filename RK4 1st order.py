import numpy as np
import matplotlib.pyplot as plt
import math

def f(x,y):
    return 5*y*math.cos(4*x)

xi,xf=0,2*math.pi
yi=0.5
n=1001
h=(xf-xi)/(n-1)
xx=[]
yy=[]
xx.append(xi)
yy.append(yi)
for i in range(n):
    k1=f(xi,yi)
    k2=f(xi+(h/2),yi+k1*(h/2))
    k3=f(xi+(h/2),yi+k2*(h/2))
    k4=f(xi+h,yi+k3*h)
    k=(k1+2*k2+2*k3+k4)/6
    x=xi+h
    y=yi+k*h
    xi=x
    yi=y
    xx.append(x)
    yy.append(y)


plt.plot(xx,yy)
plt.show()