### LIBRARIES ###

import numpy as np

### INTERSECT FUNCTION ###

S1 = input("Sequence no.1: ")
S2 = input("Sequence no.2: ")

def intersect(a,b):
	res = ""
	for n in a:
		if n in b:
			res += n
	return res

print(intersect(S1,S2))

### UNIQUE FUNCTION ###

def unique(a,b):
	ua = ""
	ub = ""
	for n in a:
		if n not in b:
			ua += n
	for n in b:
		if n not in a:
			ub += n
	return ua, ub

res = unique("axbycz","aabbcc")
print(res)

def sorting(a,b):
	s = sorted(a+b)
	res = ""
	for m in s:
		if m not in res:
			res += m
	return res


print(sorting("axbycz","aabbcc"))

### DICTIONNARY WITH TOTAL FUNCTION ###

p = float(input("price of product: "))
N = int(input("how many dealers: "))

deal = [{'name': 'Jan', 'comm': 0.05}, 
		{'name': 'Jana', 'comm': 0.15}, 
		{'name': 'Josef', 'comm': 0.25},
		{'name': 'Joe', 'comm': 0.20}, 
		{'name': 'Jim', 'comm': 0.10}, 
		{'name': 'Jiri', 'comm': 0.30},
		{'name': 'Otto', 'comm': 0.35}]

def total(num):
	ind = np.random.randint(len(deal))
	print(deal[ind]['name'])
	if num == 0:
		return p*float(1+deal[ind]['comm'])
	else:
		return float((1+deal[ind]['comm'])*total(num-1))

cm = total(N-1)
print("final price: %8.2f" %cm)


### AVER AND VAR FUNCTION ###

N = int(input("How many numbers: "))
number = np.random.randint(low = 1, high = 10, size = N)
print(number)

def aver(x):
	avA = 0
	avG = 1
	for n in x:
		avA += n
		avG *= n
	return avA/len(x), avG**(1./len(x))


def var(x):
	avV = 0
	avA = aver(x)[0]
	for n in x:
		avV += (n - avA)**2
	return avV*(1./len(x))

solution = input("What do you want to see: \n Arithmetic average tape: A \n Geometric average tape: G \n Variance tape: V \n Choice: ")

if solution == 'A': print("The arithmetic average is: %8.2f" %aver(number)[0])
elif solution == 'G': print("The geometric average is: %8.2f" %aver(number)[1])
elif solution == 'V': print("The variance is: %8.2f" %var(number))
else: print("You didn't select a goob operation")








































