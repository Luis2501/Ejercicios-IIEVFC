"""
Movimiento de Kepler (Problema 1)

Luis Eduardo Sánchez González

II Escuela de Verano de Física Computacional

lun 19 abr 2021 21:29:18 CDT 
 
Repositorio: https://github.com/Luis2501/Ejercicios-IIEVFC
"""
import sys
import numpy as np
sys.path.append("../")
from scipy.constants import G
import matplotlib.pyplot as plt
from PhysicsPy.EquationSolver import *

fig, (ax1,ax2) = plt.subplots(1, 2, figsize = (9,4.5))

#Primera parte del problema
f = lambda E: 1 + (0.0167)*np.sin(E) - E 
df = lambda E: (0.0167)*np.cos(E) - 1

Methods = [Biseccion, Newton_Rhapson, Secant]
Names = ["Bisección", "Newton Rhapson", "Secante"]
Conditions = [[1,2], 5, [1,2]]
Solutions = []

for solver_class, x0, name in zip(Methods, Conditions, Names):

	Solucion = solver_class(f, df)
	Solucion.InitialCondition(x0, tol = 1e-6, maxiter=100)
	x = Solucion.Solve()
    
	print("Solución " + name + ": ", x)
    
	Solutions.append(x)
    
Solutions = np.array(Solutions)

E = np.linspace(-5,5, 10001)

ax1.set_title("Movimiento de Kepler")
ax1.plot(E, f(E), label = "$f(E)$")
ax1.plot(Solutions, f(Solutions), "o", label = "$f(E) = 0$")
ax1.set_xlabel("Anomalia excentrica (E)") ; ax1.set_ylabel("Función f(E)")
ax1.legend(shadow=False, fancybox=True) ; ax1.grid()

del f, E

#Segunda parte del problema

t = np.linspace(0, 100, 101)

M = t*((G*(2e30 + 6e24))**(1/2))/150e9

E = np.zeros(len(M))

for i in range(len(M)):

	f = lambda E: M[i] + (0.0167)*np.sin(E) - E 
    
	Solucion = Biseccion(f, df)
	Solucion.InitialCondition([M[i] - 2, M[i] + 2], tol = 1e-6, maxiter=1000)
	E[i] = Solucion.Solve()
    
	del Solucion, f

x = np.cos(E - 0.0167)
y = np.sqrt(1-(0.0167)**2)*np.sin(E)

ax2.set_title("Órbita de la Tierra")
ax2.plot(x, y, label= r"$r(t)$", color = "purple")
ax2.set_xlabel("x (UA)") ; ax2.set_ylabel(r"y (UA)")
ax2.legend(shadow=False, fancybox=True) ; ax2.grid()

fig.tight_layout()
plt.show()
