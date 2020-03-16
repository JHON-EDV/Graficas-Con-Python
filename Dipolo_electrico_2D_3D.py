#GRAFICA DIPOLO ELECTRICO 3DB

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,5))

ax = fig.add_subplot(1,2,1,projection='3d')

u = np.linspace(0, 4 * np.pi, 700)
v = np.linspace(-np.pi, np.pi, 700)
u, v = np.meshgrid(u, v)

r = (np.abs(np.sin(u)+np.pi/2))**2
x = r*(np.sin(u) * np.cos(v))
y = r*(np.sin(u) * np.sin(v))
z = r*(np.cos(u))
plt.title('Dipolo 3D')
ax.plot_surface(x, y, z, color='#3ADF00')
ax.view_init(45,45)


plt.subplot(1,2,2)
theta = np.arange(0., 2., 0.005)*np.pi
r1= 1*(np.sin(theta+(np.pi/2)))**2
r2= 2*(np.sin(theta+(np.pi/2)))**2
r3= 3*(np.sin(theta+(np.pi/2)))**2
r4= 4*(np.sin(theta+(np.pi/2)))**2
r5= 5*(np.sin(theta+(np.pi/2)))**2
r6= 6*(np.sin(theta+(np.pi/2)))**2
r7= 7*(np.sin(theta+(np.pi/2)))**2
r8= 8*(np.sin(theta+(np.pi/2)))**2
r9= 9*(np.sin(theta+(np.pi/2)))**2


c1 = plt.subplot(122, polar=True)
c1.plot(theta, r1, color="#82FA58", linewidth=1.5)
c1.set_rmax(5.0)
c1.grid(True)

c2=plt.subplot(122, polar=True)
c2.plot(theta, r2, color="#64FE2E", linewidth=1.5)
c2.set_rmax(5.0)
c2.grid(True)

c3=plt.subplot(122, polar=True)
c3.plot(theta, r3, color="#3ADF00", linewidth=1.5)
c3.set_rmax(5.0)
c3.grid(True)

c4=plt.subplot(122, polar=True)
c4.plot(theta, r4, color="#31B404", linewidth=1.5)
c4.set_rmax(5.0)
c4.grid(True)

c5=plt.subplot(122, polar=True)
c5.plot(theta, r5, color="#298A08", linewidth=1.5)
c5.set_rmax(5.0)
c5.grid(True)

c6=plt.subplot(122, polar=True)
c6.plot(theta, r6, color="#21610B", linewidth=1.5)
c6.set_rmax(5.0)
c6.grid(True)

c7=plt.subplot(122, polar=True)
c7.plot(theta, r7, color="#21610B", linewidth=1.5)
c7.set_rmax(5.0)
c7.grid(True)

c8=plt.subplot(122, polar=True)
c8.plot(theta, r8, color="#21610B", linewidth=1.5)
c8.set_rmax(5.0)
c8.grid(True)

c9=plt.subplot(122, polar=True)
c9.plot(theta, r9, color="#21610B", linewidth=1.5)
c9.set_rmax(5.0)
c9.grid(True)

plt.title('Dipolo 2D')
plt.show()
