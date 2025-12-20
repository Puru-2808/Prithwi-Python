import numpy as np

Gate=[300,100,500,200,700,600]
Oces=[250,270,150,100,210,300]
Gate1=[]
for i in range(len(Gate)):
    if Gate[i]>=400:
        Gate1.append(Gate[i])

Oces1=[]
for i in range(len(Oces)):
    if Oces[i]>=200:
        Oces1.append(Oces[i])

add=[]
for i in range(len(Gate1)):
    add.append(Gate1[i]+Oces1[i])

a=np.sort(add)
print(a[::-1])