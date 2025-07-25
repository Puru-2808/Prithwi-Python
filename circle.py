import matplotlib.pyplot as plt
import numpy as np

# Define circle parameters
r= 6
a= 3
b= 4

# Generate theta values for circle points
theta = np.linspace(0, 2*np.pi, 200)

# Calculate x and y coordinates of circle points
x= r * np.cos( theta ) + a
y= r * np.sin( theta ) + b
       

# Plot the circle
plt.plot(x,y)

# Set labels
plt.xlabel("X")
plt.ylabel("Y")

# Set aspect ratio for a circular shape
plt.gca().set_aspect('equal')

# Set limits slightly bigger than radius and offset by center coordinates
#plt.xlim(-r - r/5  + a, r + r/5 + a)
#plt.ylim(-r - r/5  + b, r + r/5 + b)

# Set title
plt.title("Circle")

plt.show()