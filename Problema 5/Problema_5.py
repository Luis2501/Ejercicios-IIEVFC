"""
Movimientos acoplados (Problema 5)

Luis Eduardo Sánchez González

II Escuela de Verano de Física Computacional
 
Repositorio: 
"""
import numpy as np

class Aro:

	def __init__(self, k, m):

		self.k, self. m = k, m 

	def __call__(self, u, t):
	
		Phi_1, Vphi_1, Phi_2, Vphi_2, Phi_3, Vphi_3 = u
		k, m = self.k, self.m
		
		return np.array([Vphi_1, (k/m)*(-(Phi_1 - Phi_2) - (Phi_1 - Phi_3)),
				 Vphi_2, (k/m)*(-(Phi_2 - Phi_3) - (Phi_2 - Phi_1)),
				 Vphi_3, (k/m)*(-(Phi_3 - Phi_1) - (Phi_3 - Phi_2)) ])

if __name__ == "__main__":
	
	import matplotlib.pyplot as plt
	from PhysicsPy.ODEsMethods import *

	aro = Aro(k = 1, m = 1)

	Conditions = [np.pi/40, 1, np.pi/20, 1, np.pi/10, 1]

	Solucion = Runge_Kutta(aro)
	Solucion.InitialConditions(Conditions, [0, 5], 1e-3)
	Phi, t = Solucion.SolveODE()

	for k in range(0, 6, 2):

		plt.plot(t, Phi[:,k], label = f"$\phi_{k + 1}$")
	
	plt.legend(fancybox=True) ; plt.grid()
	plt.show()
