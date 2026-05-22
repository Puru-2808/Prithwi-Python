import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Figure
fig, ax = plt.subplots()
x=np.linspace(0,10,1000)
line, =ax.plot(x, np.sin(x))
ax.set_ylim(-2,2)

# Animation function
def update(frame):
    y=np.sin(x+frame/10)
    line.set_ydata(y)
    return line,

# Animation
ani = FuncAnimation(
    fig,
    update,
    frames=200,
    interval=50,
    blit=True
)

plt.show()