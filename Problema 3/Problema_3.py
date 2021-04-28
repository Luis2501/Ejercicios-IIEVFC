"""
Pozo de potencial (Problema 3)

Luis Eduardo Sánchez González

II Escuela de Verano de Física Computacional

lun 19 abr 2021 21:29:18 CDT 
 
Repositorio: https://github.com/Luis2501/Ejercicios-IIEVFC
"""
import numpy as np
from scipy.constants import e, epsilon_0

class Potencial:
    
	def __init__(self, Z):
        
		self.Z1, self.Z2 = Z - 2, 2
		self.R = (2e-15)*((self.Z1)**(1/3))
        
	def __call__(self, r):
        
		Z1, Z2, R = self.Z1, self.Z2, self.R
        
		return np.array((self.Z1*self.Z2*(e**2))/(4*np.pi*epsilon_0*r))
    
	def Force(self, r):
        
		Z1, Z2 = self.Z1, self.Z2
        
		return np.array((self.Z1*self.Z2*(e**2))/(4*np.pi*epsilon_0*(r**2)))

if __name__ == "__main__":

	import sys
	sys.path.append("../")
	import matplotlib.pyplot as plt
	from PhysicsPy.Derivation import *	

	Particula = Potencial(50)

	RR = np.linspace(Particula.R, 3*(Particula.R), 1001)

	Methods = [Forward, Central, Backward]
	Names = ["Forward", "Central", "Backward"]
	Solutions = []

	#Obtener soluciones
	for class_name in Methods:
    
		Solucion = class_name(Particula)
		Solucion.InitialConditions(RR, 1e-20)
		Fuerza = - Solucion.Solve()

		Solutions.append(Fuerza)

		del Fuerza, Solucion

	Solutions = np.array(Solutions)

	Force_Analytic = Particula.Force(RR)

	#Obtener los errores
	e_abs, e_r = [], []

	for Solution in Solutions:
    
		e_abs.append(abs(Force_Analytic - Solution))
		e_r.append(abs(Force_Analytic - Solution)/Force_Analytic)
    
	e_abs, e_r = np.array(e_abs), np.array(e_r)

	#Graficar la fuerza
	for Force, Name in zip(Solutions, Names):

		plt.plot(RR, Force, label = Name)

	plt.plot(RR, Force_Analytic, label = "Analytic Solution")

	plt.title("Fuerza que experimenta la partícula")
	plt.xlabel("Radio (r)") ; plt.ylabel("Fuerza (F)")
	plt.legend(fancybox=True) ; plt.grid()
	plt.show()
	
	#Grafica error absoluto
	for ea, Name in zip(e_abs, Names):

		plt.plot(RR, ea, label = Name)
	
	plt.title("Error absoluto")
	plt.xlabel("R") ; plt.ylabel(r"$e_{abs}$")
	plt.legend(fancybox=True) ; plt.grid()
	plt.show()

	#Grafica error relativo
	for er, Name in zip(e_r, Names):

		plt.plot(RR, er, label = Name)
	
	plt.title("Error relativo")
	plt.xlabel("R") ; plt.ylabel(r"$e_{r}$")
	plt.legend(fancybox=True) ; plt.grid()
	plt.show()
