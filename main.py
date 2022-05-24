import matplotlib.pyplot as plt
import numpy as np
ax = plt.axes(projection='3d')
x = np.linspace(-5,5,1000)
y = x**x
z = x**x
ax.plot3D(x,y.real,z.imag)
plt.show()