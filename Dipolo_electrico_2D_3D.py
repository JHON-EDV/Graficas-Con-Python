#GRAFICA DIPOLO ELECTRICO 3DB

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
	
theta = np.arange(0., 2., 0.005)*np.pi
Color=["#82FA58","#82FA58","#64FE2E","#3ADF00","#31B404","#298A08","#21610B","#21610B","#21610B","#21610B","#21610B"]

def main():	
	grafica3d()
	
	

def grafica3d():
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
	
	grafica2d()

def grafica2d():

	for i in range(1,9):
		r=i*(np.sin(theta+(np.pi/2)))**2

		c=plt.subplot(122, polar=True)
		c.plot(theta,r,Color[i], linewidth=1.5)

	plt.title('Dipolo 2D')
	plt.show()


if __name__ == '__main__':
	main()