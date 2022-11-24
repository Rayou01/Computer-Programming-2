import numpy as np

def convertHex(x):
  if x==-1:
    x =input("New Two-digit hexa-number #1: ")
  try:
    out = int(x, base=16)
  except:
    print(str(x) + "is an incorrect Two-digit hexa-number")
    out=convertHex(-1)
  finally:
    return out

A=input("Two-digit hexa-number #1: ")
O=input("Operation [+,-,*,/]: ")
B=input("Two-digit hexa-number #2: ")
HexA=convertHex(A)
HexB=convertHex(B)
out=0

if O=='+':
  out_dec=HexA+HexB
  print("A+B (dec) = %d" %out_dec)
  out_hex = hex(out_dec)
  print("A+B(hex) = ", end='')
  print(out_hex)
elif O=='-':
  out_dec=HexA-HexB
  print("A-B (dec) = %d" %out_dec)
  out_hex = hex(out_dec)
  print("A-B(hex) = ", end='')
  print(out_hex)
elif O=='*':
  out_dec=HexA*HexB
  print("A*B (dec) = %d" %out_dec)
  out_hex = hex(out_dec)
  print("A*B(hex) = ", end='')
  print(out_hex)
elif O=='/':
  try:
    out_dec=HexA/HexB
  except:
    print("Division by 0 is not possible")
    out=-1
  else:
    print("A/B (dec) = %d" %out_dec)
    out_hex = hex(out_dec)
    print("A/B(hex) = ", end='')
    print(out_hex)
else:
  print("Incorrect sign of operation")

#//print("Result =" + str(out))

try:
	f = open("input_file.txt", 'r', encoding = 'utf-8')
except:
	print("File not found")
else:
	S = f.read()
	print(S)
finally:
	f.close()

S = S.replace('.', '')
print(S)
A = S.split(' ')
print(A)
B = []
for i in A:
	if i.lower() not in B:
		B.append(i.lower())

print(B)

def poem(dictionnary, lines, words):
  out = ["" for i in range(lines)]
  for i in range(lines):
    line = ""
    for j in range(words):
      n = np.random.randint(len(dictionnary))
      line = line + str(dictionnary[n]) + ' '
    out[i] = line
  return out

print(poem(B, 2, 3))
