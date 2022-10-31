import numpy as np
import matplotlib.pyplot as pt

### ROSENBROCK IN PYTHON ###
#F(x,y) = 100(y-x**2)**2+(1-x)**2

def rb(x,y):
	return 100*(y-x**2)**2+(1-x)**2

### WIREFRAME CHART ###

N = 40
x = np.linspace(start = -2, stop = 2, num = N)
y = np.linspace(start = -1, stop = 3, num = N)

F = np.zeros((N,N))
for m in range(N):
	for n in range(N):
		F[m,n] = rb(x[m], y[n])

fig = pt.figure()
ax = fig.gca(projection = '3d')
ax.plot_wireframe(x, y, F, rstride = 10, cstride = 10)
pt.show()

### GOLDEN CUT ###

t = 2/(1+np.sqrt(5))
A = 4
x1 = 1
y_min = -1
y_max = 3

y = [0, 1-t, t, 1]
f = np.zeros(A)
for n in range(A):
	y[n] = y_min + y[n]*(y_max - y_min)
	f[n] = rb(x1, y[n])

for n in range(100):	#100 is a random value
	if f[1] >= f[2]:
		y[0:2] = y[1:3]
		y[2] = y[0] + t*(y[3] - y[0])
		f[0:2] = f[1:3]
		f[2] = rb(x1, y[2])
	else:
		y[2:4] = y[1:3]
		y[1] = y[0] + (1-t)*(y[3] - y[0])
		f[2:4] = f[1:3]
		f[1] = rb(x1, y[1])

print("y_min = %6.2f" %y[1])	# It prints y_min = 1.0
print("f_min = %6.2f" %f[1])	#It prints f_min = 0.0

### STEEPEST DESCENT ###

h = 1e-3
a = h
x = [-1, 1]
M = 10000

g = np.zeros(2)

for m in range(M):
	g[0] = (rb(x[0]+h,x[1]) - rb(x[0]-h,x[1])) / (2*h)
	g[1] = (rb(x[0],x[1]+h) - rb(x[0],x[1]-h)) / (2*h)

	x[0] -= a*g[0]
	x[1] -= a*g[1]

print(x)	#It prints [0.9922973295157226, 0.984623821895644] ≈ [1,1] => Same result that the Golden cut


### MATYAS FUNCTION ###

def mt(x1,x2):
	return 0.26*(x1**2+x2**2) - 0.48*x1*x2

### CONTOUR CHART ###

N = 100
x = np.linspace(start = -10, stop = 10, num = N)
y = np.linspace(start = -10, stop = 10, num = N)

F = np.zeros((N,N))
for m in range(N):
	for n in range(N):
		F[m,n] = mt(x[m], y[n])

fig = pt.figure()
ax = fig.gca(projection = '3d')
ax.contour(x, y, F, N)
pt.show()

### GOLDEN CUT ###

t = 2/(1+np.sqrt(5))
A = 4
x1 = 0
y_min = -1
y_max = 3

y = [0, 1-t, t, 1]
f = np.zeros(A)
for n in range(A):
	y[n] = y_min + y[n]*(y_max - y_min)
	f[n] = mt(x1, y[n])

for n in range(100):	#100 is a random value
	if f[1] >= f[2]:
		y[0:2] = y[1:3]
		y[2] = y[0] + t*(y[3] - y[0])
		f[0:2] = f[1:3]
		f[2] = mt(x1, y[2])
	else:
		y[2:4] = y[1:3]
		y[1] = y[0] + (1-t)*(y[3] - y[0])
		f[2:4] = f[1:3]
		f[1] = mt(x1, y[1])

print("y_min = %6.2f" %y[1])	# It prints y_min = 0.0
print("f_min = %6.2f" %f[1])	#It prints f_min = 0.0

### STEEPEST DESCENT ### 

h = 1e-3
a = h
x = [-1, 1]
M = 10000

g = np.zeros(2)

for m in range(M):
	g[0] = (mt(x[0]+h,x[1]) - mt(x[0]-h,x[1])) / (2*h)
	g[1] = (mt(x[0],x[1]+h) - mt(x[0],x[1]-h)) / (2*h)

	x[0] -= a*g[0]
	x[1] -= a*g[1]

print(x)	#It prints [-4.517334597734899e-05, 4.5173345976747654e-05]

### NEWTON METHOD FOR MATHYAS FUNCTION ###

h = 1e-3
x = [-1, 1]
M = 10

g = np.zeros(2)
G = np.zeros((2,2))

for m in range(M):
	g[0] = (mt(x[0]+h,x[1]) - mt(x[0]-h,x[1])) / (2*h)
	g[1] = (mt(x[0],x[1]+h) - mt(x[0],x[1]-h)) / (2*h)

	G[0,0] = mt(x[0]+2*h,x[1]) - 2*mt(x[0],x[1]) + mt(x[0]-2*h,x[1])
	G[0,1] = mt(x[0]+h,x[1]+h) - mt(x[0]-h,x[1]+h) - mt(x[0]+h,x[1]-h) + mt(x[0]-h,x[1]-h)
	G[1,0] = G[0,1]
	G[1,1] = mt(x[0],x[1]+2*h) - 2*mt(x[0],x[1]) + mt(x[0],x[1]-2*h)
	G = G / (4*h**2)

	x = x - np.matmul( np.linalg.inv(G), g)

print(x)	#It prints [0.0, 0.0]

### THREE-HUMP CAMEL FUNCTION ###

def thc(x1,x2):
	return 2*x1**2 - 1.05*x1**4 + (x1**6)/6 + x1*x2 + x2**2

N = 100
x = np.linspace(start = -10, stop = 10, num = N)
y = np.linspace(start = -10, stop = 10, num = N)

F = np.zeros((N,N))
for m in range(N):
	for n in range(N):
		F[m,n] = thc(x[m], y[n])

fig = pt.figure()
ax = fig.gca(projection = '3d')
ax.contour(x, y, F, N)
pt.show()

### NEWTON METHOD FOR THREE-HUMP CAMEL FUNCTION ###

h = 1e-3
x = [0, 1]
M = 10

g = np.zeros(2)
G = np.zeros((2,2))

for m in range(M):
	g[0] = (thc(x[0]+h,x[1]) - thc(x[0]-h,x[1])) / (2*h)
	g[1] = (thc(x[0],x[1]+h) - thc(x[0],x[1]-h)) / (2*h)

	G[0,0] = thc(x[0]+2*h,x[1]) - 2*thc(x[0],x[1]) + thc(x[0]-2*h,x[1])
	G[0,1] = thc(x[0]+h,x[1]+h) - thc(x[0]-h,x[1]+h) - thc(x[0]+h,x[1]-h) + thc(x[0]-h,x[1]-h)
	G[1,0] = G[0,1]
	G[1,1] = thc(x[0],x[1]+2*h) - 2*thc(x[0],x[1]) + thc(x[0],x[1]-2*h)
	G = G / (4*h**2)

	x = x - np.matmul( np.linalg.inv(G), g)
 
print(x)	#It prints [1.69983937e-20 5.96869538e-20] = [0, 0]





