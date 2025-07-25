import numpy as np
import matplotlib.pyplot as plt

xi=-1
xf=1
yi=0
yf=0
n=10001
h=(xf-xi)/(n-1)

Ei=0
Ef=15
n1=1001
h1=(Ef-Ei)/(n1-1)

EE=[]
EE1=[]
xx=[]
xx1=[]
yy=[]
yy1=[]
mm=[]
mm1=[]

for i in range(n1):
    zi=1
    yi=0
    E=Ei+i*h1
    EE.append(E)
    mi=-2*E*yi
    mm.append(mi)
    for j in range(n):
        x=xi+j*h
        z=zi+h*mm[i]
        y=yi+h*zi
        m=-2*EE[i]*y
        yi=y
        zi=z
        mm[i]=m
    xx.append(x)
    yy.append(y)

for i in range(n1-1):
    if yy[i]*yy[i+1]<0:
        EE1.append(EE[i])


for i in range(len(EE1)):
     mi1=-2*EE1[i]*yi
     mm1.append(mi1)

for i in range(len(mm1)):
     yi=0
     zi1=1
     for j in range(n):
        x1=xi+j*h
        z1=zi1+h*mm1[i]
        y1=yi+h*zi1
        m1=-2*EE1[i]*y1
        yi=y1
        mm1[i]=m1
        zi1=z1
        xx1.append(x1)
        yy1.append(y1)
     plt.plot(xx1,yy1)
plt.grid()
plt.show()