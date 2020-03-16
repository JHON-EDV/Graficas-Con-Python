#Jhon Edison Vargas 20152005077
#Andres Ariza       201520050

# Grafica del Cuadripolo electrico en 3D

#Importar librerias
import numpy as np
import matplotlib.pyplot as ploty
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



fig = ploty.figure()
ax = fig.gca(projection='3d')
phi = np.linspace(-np.pi,np.pi,200)
theta = np.linspace(0, 2 * np.pi, 200)
theta, phi = np.meshgrid(theta, phi)
r = np.abs((np.sin(phi+np.pi/2))**2)

e_x = r*(np.cos(theta) * np.sin(phi))
e_y = r*(np.sin(theta) * np.sin(phi))
e_z = r*(np.cos(phi))

ax.plot_surface(e_x, e_y, e_z, rstride=1, cstride=1, cmap=cm.jet)

ax.plot(e_x, e_z, zdir='e_z',zs=1.5)
#ax.plot(e_y, e_z, zdir='e_x',zs=-0.5)
#ax.plot(e_x, e_y,  zdir='e_y',zs=-1.5)

ploty.title("DIPOLO EN 2D y 3D") 
ploty.show()
