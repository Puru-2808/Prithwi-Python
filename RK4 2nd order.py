import numpy as np
import matplotlib.pyplot as plt
import math

def f(t,x,u):
    return -2*b*u - w0**2*x 

b=1
w0=4
T=(2*math.pi)/w0
ti,tf=0,4*T
xi=10
ui=0
n=1001
h=(tf-ti)/(n-1)
tt=[]
xx=[]
tt.append(ti)
xx.append(xi)
for i in range(n):
    k1=ui
    j1=f(ti,xi,ui)
    k2=ui+(h/2)*j1
    j2=f(ti+(h/2),xi+k1*(h/2),ui+j1*(h/2))
    k3=ui+(h/2)*j2
    j3=f(ti+(h/2),xi+k2*(h/2),ui+j2*(h/2))
    k4=ui+j3*h
    j4=f(ti+h,xi+k3*h,ui+j3*h)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    
    t=ti+h
    x=xi+k*h
    u=ui+j*h
    ti=t
    xi=x
    ui=u
    tt.append(t)
    xx.append(x)


plt.plot(tt,xx)
plt.show()