"""
Movimientos acoplados (Problema 5)

Luis Eduardo Sánchez González

II Escuela de Verano de Física Computacional

lun 19 abr 2021 21:29:18 CDT 
 
Repositorio: 
"""
import numpy as np

class Carga:
    
    def __init__(self, sigma_0, a):
        
        self.sigma_0, self.a = sigma_0, a
        
    def __call__(self, r):
        
        sigma_0, a = self.sigma_0, self.a
        
        return np.array(sigma_0*(1 - (r**2/a**2))*2*np.pi*r)

if __name__ == "__main__":

	import sys
	sys.path.append("../")
	import matplotlib.pyplot as plt
	from PhysicsPy.Integration import *	

	Cilindro = Carga(1.3e-6, 1e-3)

	Methods = [Riemann, Trapeze, Midpoint, Simpson1_3, Simpson3_8]
	Names = ["Riemman", "Trapeze", "Midpoint", "Simpson1_3", "Simpson3_8"]
	Solutions = []

	print("Soluciones númericas \n")

	for class_name, name in zip(Methods, Names):
    
		Solucion = class_name(Cilindro)
		Solucion.Limits(0, Cilindro.a, 1e-7)
		Integral = Solucion.Solve()

		Solutions.append(Integral)
    
		print(name + " Integration: ", Integral)

		del Integral, Solucion
    
	Solutions = np.array(Solutions)

	Q_total = (Cilindro.sigma_0*np.pi*(Cilindro.a**2))/2

	print("\nSolución analítica: ", Q_total)

	#Error absoluto y error relativo
	e_abs = Q_total - Solutions
	e_r = (Q_total - Solutions)/Q_total

	print("\nMétodo \t \t", "Error absoluto \t\t", "Error relativo \t\t", "Error Porcentual \n")

	for i in range(len(Solutions)):
    
		print(Names[i], "\t", e_abs[i], "\t", e_r[i], "\t ", e_r[i]*100, "%")
