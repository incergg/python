#4.2
w = 10 #input("Dlugosc miarki: ")
def miarka (n):
	m=""
	for x in range(int(n)):
		m+="|...."
	m+="|\n0"
	for x in range(int(n)):
		for y in range(5-len(str(x+1))):
			m+=" "
		m+=str(x+1)	
	return m

print (miarka(w))



a = 3  #wysokosc
b = 4  #dlugosc
def kratka(n,m):
	k=""
	for x in range(n):
		for y in range(m):
			k+="+---"
		k+="+\n"
		for y in range(m):
			k+="|   "
		k+="|\n"
	for x in range(m): 
		k+="+---"
	k+="+\n"
	return(k)

print(kratka(a,b))

#4.3

def factorial(n):
	
	x=1
	for each in range(1,n+1):
		x=x*each
	return x
print (factorial(5))



#4.4
def fibonacci(n):                                                                                                 
	if(n==0):
		return 0
	else:
		x=0
		y=1
		for i in range(1,n):
			z=(x+y)
			x=y
			y=z
	return y
	
	
print(fibonacci(6),fibonacci(16))


#4.5 

def odwracanie(L,left,right):
	while left < right:
		temp = L[left]
		L[left] = L[right]
		L[right]=temp
		left+=1
		right-=1

l = [1,2,3,4,5,6]
odwracanie(l, 0, 4)
print(l)

#4.6

def sum_seq(sequence):
	sum=0
	if isinstance(sequence, (list, tuple)):
		for el in sequence:
			sum+=sum_seq(el)
	else :
		return sequence
	return sum
seq= [[1],[1,2],(3,2),[2,2,2,3]]
print(sum_seq(seq))



#4.7

def flatten(sequence):
	fl=[]
	if isinstance(sequence, (list,tuple)):
		for el in sequence:
			if isinstance(el, (list,tuple)):
				fl+=flatten(el)
			else:
				fl.append(el)
	return fl
	
sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print (flatten(sequence))
