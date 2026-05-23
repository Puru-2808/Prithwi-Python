import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
theta=np.pi/6
u=20
g=9.8
T=2*u*np.sin(theta)/g
R=u**2*np.sin(2*theta)/g
H=(u**2*(np.sin(theta))**2)/(2*g)
line,=ax.plot([],[],'ro')
ax.set_xlim(0,R)
ax.set_ylim(0,H)

def update(frame):
    t=frame
    x=u*np.cos(theta)*t
    y=u*np.sin(theta)*t-0.5*g*t**2
    line.set_data([x],[y])
    return line,

N=200
ani=FuncAnimation(
    fig,
    update,
    frames=np.linspace(0,T,N),
    interval=(T*1000)/N,
    blit=False
)

plt.show()