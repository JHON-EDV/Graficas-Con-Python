#JHON EDISON VARGAS VARGAS 20152005077
#GRAFICA CUADRUPOLO ELECTRICO 3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,2,1,projection='3d')

#plt.subplot(1,2,1)
u = np.linspace(0, 4 * np.pi, 700)
v = np.linspace(-np.pi, np.pi, 700)
u, v = np.meshgrid(u, v)

r = np.abs(np.sin(u+np.pi/2))*(np.abs(np.cos(u+np.pi/2))**(1/2))
x = r*(np.sin(u) * np.cos(v))
y = r*(np.sin(u) * np.sin(v))
z = r*(np.cos(u))
plt.title('Cuadripolo 3D')
ax.plot_surface(x, y, z, color='#DF0101')
ax.view_init(30,45)


plt.subplot(1,2,2)
plt.title("Cuadripolo electrico en 2D")

phi=np.linspace(0, np.pi, 100)
theta=(np.arange(0,2*np.pi,0.01))


r1 = 1*(abs(np.sin(theta)))
r2 = 2*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)
r3 = 3*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)
r4 = 4*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)
r5 = 5*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)
r6 = 6*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)
r7 = 7*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)
r8 = 8*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)

c1 = plt.subplot(122, polar=True)
c1.plot(theta,r1, color="blue", linewidth=2)
c1.set_rmax(5.0)
c1.grid(True)

c2 = plt.subplot(122, polar=True)
c2.plot(theta,r2, color="green", linewidth=2)
c2.set_rmax(5.0)
c2.grid(True)

c3 = plt.subplot(122, polar=True)
c3.plot(theta,r3, color="#DF0101", linewidth=2)
c3.set_rmax(5.0)
c3.grid(True)

c4 = plt.subplot(122, polar=True)
c4.plot(theta,r4, color="#DF0101", linewidth=2)
c4.set_rmax(5.0)
c4.grid(True)

c5 = plt.subplot(122, polar=True)
c5.plot(theta,r5, color="#DF0101", linewidth=2)
c5.set_rmax(5.0)
c5.grid(True)

c6 = plt.subplot(122, polar=True)
c6.plot(theta,r6, color="#DF0101", linewidth=2)
c6.set_rmax(5.0)
c6.grid(True)

c7 = plt.subplot(122, polar=True)
c7.plot(theta,r7, color="#DF0101", linewidth=2)
c7.set_rmax(5.0)
c7.grid(True)

c8 = plt.subplot(122, polar=True)
c8.plot(theta,r8, color="orange", linewidth=2)
c8.set_rmax(5.0)
c8.grid(True)
#plt.legend(loc=1) 
plt.title('Cuadripolo 2D')
plt.show()
