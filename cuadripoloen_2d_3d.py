#Jhon Edison Vargas 20152005077
#Andres Ariza       201520050
# Grafica del Cuadripolo electrico en 3D

#Importar librerias
import matplotlib.pyplot as pyplot 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D  

# Se crea una figura 3D
fig = pyplot.figure("Cuadripolo en 3D") 
ax = fig.gca(projection='3d')
u = np.linspace(0, 4 * np.pi, 700)
v = np.linspace(-np.pi, np.pi, 700)
u,v = np.meshgrid(u, v)

# Se crea la funcion de la grafica 3D / f(x,y,z)
r=((np.abs(np.sin(u)))*((np.abs(np.cos(u)))**1/2)) 
x = r*(np.sin(u) * np.cos(v)) 
y = r*(np.sin(u) * np.sin(v)) 
z = r*(np.cos(u))
ax.plot_surface(x, y,z)
ax.plot(x, z, zdir='z',zs=0.2)
#color="teal"
# Se pone titulo a la grafica y se muestra por pantalla 
pyplot.title("CUADRIPOLO EN 2D y 3D") 
pyplot.show()
