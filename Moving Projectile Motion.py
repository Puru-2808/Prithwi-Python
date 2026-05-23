import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# initial value of states position and velocity
angle=0
theta=(np.pi/180)*angle
u=50  
g=9.8
h=1.651
dt=0.01
x=0
y=h
t=0
xt=[]
yt=[]
tt=[]
vx=u*np.cos(theta)
vy=u*np.sin(theta)


fig,ax=plt.subplots()
line,=ax.plot([],[],'r-')
point,=ax.plot([],[],'bo')
ax.set_xlim(0,100)
ax.set_ylim(0,200)


def update(frame):
    global x,y,vx,vy,t
    x=x+vx*dt
    y=y+vy*dt
    vy=vy-g*dt
    t=t+dt
    xt.append(x)
    yt.append(y)
    tt.append(t)
    line.set_data(xt,yt)
    point.set_data([x],[y])
    R=xt[-1]
    H=yt[-1]
    T=tt[-1]
    if y<=0.001:
        print("Time of flight:",T)
        print("Range:",R)
        print("Max height:",max(yt))
        ani.event_source.stop()
    return line,point

ani=FuncAnimation(
    fig,
    update,
    interval=dt*1000,
    blit=False
)

plt.show()