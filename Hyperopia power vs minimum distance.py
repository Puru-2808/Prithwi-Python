# Hyperopia
import matplotlib.pyplot as plt
import numpy as np

xi=0.01
xf=2
n=1001
u=-25               #minimum distance normal human can see in cm
h=(xf-xi)/(n-1)
pp=[]
vv=[]
for i in range(n):
    p=xi+i*h
    pp.append(p) # power
    f=(1/p)*100   # focus in cm
    v=(u*f)/(u+f)
    vv.append(abs(v))   # v in cm

plt.plot(pp,vv)
plt.xlabel("power")
plt.ylabel("minimum distance they can see")
plt.grid()
plt.show()