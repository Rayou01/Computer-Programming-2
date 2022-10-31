### LiBRARIES ###
import numpy as np
import math as mt
from matplotlib import pyplot as pt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

N = 5
x = np.random.randint( low = 0, high = 100, size = N)	#first vector
y = np.random.randint( low = 0, high = 100, size = N)	#second vector
print(x)
print(y)

### WITH NUMPY FUNCTIONS ###
tab = [x, y]
print( np.sum(tab, axis = 0))	#summe of both vectors
print(np.divide(x, y))	#ratio of both vectors
print(np.subtract(x, y))
print(np.multiply(x, y))

### WITHOUT NUMPY FUNCTIONS ###
add = x+y
print(add)
minus = x-y
print(minus)
mult = x*y
print(mult)
divide = x/y
print(divide)

### WITH COS, SIN AND TAN FUNCTIONS ###

N = 20
phi = np.linspace(start = -mt.pi, stop = mt.pi, num = N)

y1, y2, y3 = np.zeros(N), np.zeros(N), np.zeros(N)
for n in range(N):
	y1[n] = mt.sin(phi[n])
	y2[n] = mt.cos(phi[n])
	y3[n] = mt.tan(phi[n]) #or y3[n] = mt.divide(y1[n], y2[n])

#To see each functions on the graph
pt.plot(phi, y1)
pt.plot(phi, y2)
pt.plot(phi, y3)
#pt.show()

### EVEN, ODD AND POSITIVE, NEGATIVE NUMBERS ###

x = np.random.randint(low = -10, high = 10)	#integer x from the interval <-10 ; 10>
print(x)


if x%2==0:	#modulo
	print("even number")
else:
	print("odd number")
if x<0:
	print("negative number")
else:
	print("positive number")
	

### SORT AN ARRAY ###

N = 10
x = np.random.randint( low = 0, high = 100, size = N)
y = np.sort(x)
print(y)

#Bubble sorting : min to max
for n in range(1, N):
	for k in range(N-1):
		if(x[k] > x[k+1]):
			x[k],x[k+1] = x[k+1], x[k]
print(x)

#Bubble sorting : max to min
for n in range(1, N):
	for k in range(N-1):
		if(x[k] < x[k+1]):	#The only difference is the sign of the inequality in the if loop
			x[k],x[k+1] = x[k+1], x[k]
print(x)

#Bubble sort : array <-50; 50>
x = np.random.randint( low = -50, high = 50, size = N)
y = np.sort(x)
print(y)

### TWO-DIMENSIONAL ROSENBROCK ###

N = 20

x = np.linspace(start = -2, stop = 2, num = N)
y = np.linspace(start = -3, stop = 3, num = N)

F = np.zeros((N,N))
for m in range(N):
	for n in range(N):
		F[m,n] = (1-x[m])**2 + 100*(y[n]-x[m]**2)**2

# Plot the surface.

fig = pt.figure()	#Create a figure
ax = fig.gca(projection= '3d')	#The figure is in 3d

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()





