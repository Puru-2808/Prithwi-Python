import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# initial value of states position and velocity
angle=90
theta=(np.pi/180)*angle
u=(11.2)*1000
G=6.674*10**(-11)
M=5.972*10**(24)
Re=6.371*10**6
g=G*M/(Re**2)
h=0
dt=1
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
ax.set_xlim(0,1000000)
ax.set_ylim(0,2000000)


def update(frame):
    global x,y,vx,vy,g,t
    x=x+vx*dt
    y=y+vy*dt
    g=G*M/(Re+y)**2
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
    if y<=0.001 and t>0:
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