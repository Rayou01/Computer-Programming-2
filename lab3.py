### STRINGS ###


### NUMBER OF WORDS ###

S = "aa b ccc x z ddd"
words = 1
for m in range(len(S)):
	if S[m] == ' ':
		words += 1

print("The number of words: %d" %words)

### SORT WORDS IN ALPHABETICAL ORDER ###

W = S.split(' ')
for m in range(words):
	for n in range(m, words):
		if W[m] > W[n]:
			W[m], W[n] = W[n], W[m]
print(W)

### ODD/EVEN NUMBER OF WORDS ###

if words%2 == 0:	
	W.sort(reverse=True)
	print("even number of words %d" %words)
else:
	W.sort();
	print("odd number of words %d" %words)
print(W)



S = "AaBCccXZDdd"
words = 0

for m in S:
	if m.isupper():	#m >= 'A' and m <= 'Z'
		words += 1

L = ""
B = 0
for m in range(1,len(S)):
	if 'A' <= S[m] <= 'Z':
		L += S[B:m] + " "
		B = m
	elif m == len(S) -1:
		L += S[B:m+1]

print(L)
C = L.lower()
print(C)
print("The number of words %d" %words)

W = C.split()
W_swap = W[::-1]
#W.reverse()
print("Swaped: %s" %W_swap)



beer = [{'brand': 'tuborg', 'price': 50.0, 'quality': 5}, 
		{'brand': 'pilsen', 'price': 40.0, 'quality': 3}, 
		{'brand': 'reznak', 'price': 30.0, 'quality': 2},
		{'brand': 'aaa', 'price': 33.0, 'quality': 1},
		{'brand': 'bcd', 'price': 90.0, 'quality': 4},]

a = sorted(beer, key = lambda param: param["quality"])
print(a)

b = sorted(beer, key = lambda param: param["price"])
print(b)

c = sorted(beer, key = lambda param: param['price']/param['quality'])
print(c)












