### IMPORT ###

import math as mt
import numpy as np
import matplotlib.pyplot as plt


### DEF OF FUNCTIONS ###

def f1(x):
	return mt.sin(x)+x**2-1.5*x+1

def f2(x):
	return 10+(x**2-10*mt.cos(2*mt.pi*x))

def f3(x):
	return (mt.sin(3*mt.pi*x))**2 + (x-1)**2

def f4(x):
	return 0.5 + ((mt.sin(x**2))**2 - 0.5)/(1+0.001*x**2)**2


### INTEGRATION WITH RECTANGLE RULE FOR f1 ###

N = 100
L = [0,4]
S = (L[1]-L[0])/N 
s = 0
for n in range(N):
	s += f1(S/2 + n*S)
s *= S

print("F1 = %8.2f" %s)


### INTEGRATION WITH RECTANGLE RULE FOR f2 ###

N = 100
L = [-5,0]
L1 = [0,5]
S = (L[1]-L[0])/N 
S1 = (L1[1]-L1[0])/N 
s = 0
s1 = 0

for n in range(N):
	s += f2(S/2 + n*S)
s *= S

for n in range(N):
	s1 += f2(S1/2 + n*S1)
s1 *= S1

s += s1

print("F2 = %8.2f" %s)


### INTEGRATION WITH TRAPEZOIDAL RULE FOR f3###

N = 100
L = [0,5]
S = (L[1]-L[0])/N 
s = 0
for n in range(N):
	s += (f1(S*(n+1))+f1(n*S))/2
s *= S

print("F3 = %8.2f" %s)


### INTEGRATION WITH TRAPEZOIDAL RULE FOR f4###

N = 100
L = [-10,0]
L1 = [0,10]
S = (L[1]-L[0])/N 
S1 = (L1[1]-L1[0])/N 
s = 0
s1 = 0

for n in range(N):
	s += (f4(S*(n+1))+f4(n*S))/2
s *= S

for n in range(N):
	s1 += (f4(S1*(n+1))+f4(n*S1))/2
s1 *= S1

s += s1 
print("F4 = %8.2f" %s)


### CONVERSION DECIMAL TO BINARY ###

def conv_DecToBin(x):
	if x == 0:
		return ''
	return conv_DecToBin(x//2) + str(x%2)


### CONVERSION BINARY TO DECIMAL ###

def binaryToDecimalConvert(array):
	decimal = 0
	power = len(array) - 1

	for item in array:
		decimal += pow(2, power) * item
		power -= 1
	return decimal


### CONVERSION BINARY TO HEXADECIMAL ###

def conv_binary_to_hexadecimal():
	binary = []
	number = input("Please enter a binary number to convert into hexa: ")	#User enter a binary number
	for item in number:
		binary.append(int(item))	#Append this number in an array

	print("Binary number is " + str(binary))
	print()	#Go to next line

	#check if divisible by 4
	if (len(binary) % 4) == 1:	#Need 3 x 0 to have 4 bits
		for index in range(0,3):
			binary.insert(0,0)	#Insert at the beginning some 0s to have the correct number of bits
	elif (len(binary) % 4) == 2:	#Need 2 x 0
		for index in range(0,2):
			binary.insert(0,0)
	elif (len(binary) % 4) == 3:	#Need one 0
		for index in range(0,1):
			binary.insert(0,0)

	print("Now, the binary number is " + str(binary))
	print()

	number_holder = []
	decimal_set = []
	hex_number = ""

	while (len(binary) != 0):
		for index in range(0,4):
			number_holder.append(binary.pop(0)) #remove the first index of the binary number and adds it to number_holder
		decimal_set.append(binaryToDecimalConvert(number_holder))
		number_holder = []
		print("The decimal numbers according to is " +str(decimal_set))

	#Convert all portions of decimal set into hex and add it to the hex_number

	for index in decimal_set:
		if index == 10:
			hex_number += "A"
		elif index == 11:
			hex_number += "B"
		elif index == 12:
			hex_number += "C"
		elif index == 13:
			hex_number += "D"
		elif index == 14:
			hex_number += "E"
		elif index == 15:
			hex_number += "F"
		else:
			hex_number += str(index)

	print("The hexadecimal number is ")
	return hex_number

print("The binary number for 49 is " + str(conv_DecToBin(49)))
print("The binary number for 113 is " + str(conv_DecToBin(113)))
print(conv_binary_to_hexadecimal())
print(conv_binary_to_hexadecimal())

### ELECTRICAL POTENTIAL ###

N = 10
f1 = -1
f2 = 1

C = np.zeros((N-1,N-1))
C[0,0] = -2
C[0,1] = 1
for n in range(1,N-2):
  C[n,n-1] = 1
  C[n,n] = -2
  C[n,n+1] = 1
C[N-2,N-3] = 1
C[N-2,N-2] = -2

print(C)

R = np.zeros(N-1)
R[0] = -f1
R[N-2] = -f2

fi = np.zeros(N+1)
fi[1:N] = np.linalg.solve(C,R)
fi[0] = f1
fi[N] = f2
plt.plot(fi)


### matlab - matlab result - python - python result ###

