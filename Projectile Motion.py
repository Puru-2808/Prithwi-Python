import numpy as np
import matplotlib.pyplot as plt

g=9.8
u=20
theta=np.radians(45)

t=np.linspace(0,3,100)

x=u*np.cos(theta)*t
y=u*np.sin(theta)*t - 0.5*g*t**2

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Projectile Motion")
plt.grid()
plt.show()