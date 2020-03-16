#JHON EDISON VARGAS VARGAS 20152005077
#GRAFICA CUADRUPOLO ELECTRICO 3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,2,1,projection='3d')
phi=np.linspace(0, np.pi, 100)
theta=(np.arange(0,2*np.pi,0.01))
Color=["blue","green","green","#DF0101","#DF0101","#DF0101","#DF0101","orange"]

#plt.subplot(1,2,1)

def grafica3d():
	u = np.linspace(0, 4 * np.pi, 800)
	v = np.linspace(-np.pi, np.pi, 800)
	u, v = np.meshgrid(u, v)

	r = np.abs(np.sin(u+np.pi/2))*(np.abs(np.cos(u+np.pi/2))**(1/2))
	x = r*(np.sin(u) * np.cos(v))
	y = r*(np.sin(u) * np.sin(v))
	z = r*(np.cos(u))

	plt.title('Cuadripolo 3D')
	ax.plot_surface(x, y, z, color='#DF0101')
	ax.view_init(30,45)
	grafia2d()

def main():
	grafica3d()

def grafia2d():
	plt.subplot(1,2,2)
	plt.title("Cuadripolo electrico en 2D")

	r1 = 0.9*(abs(np.sin(theta)))
	c1 = plt.subplot(122, polar=True)
	c1.plot(theta,r1,"blue", linewidth=2)
	for i in range(2,8):

		r=i*(abs(np.sin(theta)))*((abs(np.cos(theta)))**0.5)	
		c = plt.subplot(122, polar=True)
		c.plot(theta,r, Color[i], linewidth=2)

	c.set_rmax(5.0)
	c.grid(True)
	plt.title('Cuadripolo 2D')
	plt.show()


#plt.legend(loc=1) 


if __name__ == '__main__':
	main()
