#3.1
print("ZADANIE 3.1")
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;    #nie widze problemu skladniowego w podanym przykladzie, jedynie fakt iz result to zawsze y chyba ze x>y


for i in "qwerty": 
	if ord(i) < 100: print(i)  # if przenosimy do kolejnej lini zaznaczajac hierarchie 
	
	
#for i in "axby": print ord(i) if ord(i) < 100 else i   # if nie moze zostac uzyte po frazie ktora warunkujemy
for i in "axby": 
	if (ord(i)<100):
		print (ord(i)) 
	else:
		print (i)


#3.2
print("\nZADANIE 3.2")
#Co jest złego w kodzie:
#L = [3, 5, 4] ; L = L.sort()     #operacja powinna byc przeprowadzona bezposrednio na liscie L.sort()
#x, y = 1, 2, 3                   #3 nie jest przypisana do zmiennej
#X = 1, 2, 3 ; X[1] = 4				#krotek nie mozemy edytowac 
#X = [1, 2, 3] ; X[3] = 4			#indeks poza listą 
#X = "abc" ; X.append("d")			#string nie ma funkcji append
#map(pow, range(8))			  		#podano tylko 1 argument funkcji pow()


L = [3, 5, 4] ; L.sort() ; print(L)
x, y = 1, 2 #,3
X = 1, 2, 3 ; print(X) #X[1] = 4 
X = [1, 2, 3] ; X[2] = 4 ; print(X)
X = "abc" ; X+="d" ; print(X)#X.append("d")

X = list(map(pow, range(8),range(8))) ; print (X)



#3.3
print("\nZADANIE 3.3")
for x in range(31):
	if x%3!=0:
		print(x)
		
#3.4
print("\nZADANIE 3.4")
while True:
	try:
		a = (input("Liczba: "))
		n=int(a)
		print(n,pow(n,3))
		
	except ValueError:
		if(a == "stop"):
			break
		print ("Blad, podaj liczbe!")

#3.5
print("\nZADANIE 3.5")
a = input("Dlugosc miarki: ")
m = ""
for x in range(int(a)):
	m+="|...."
m+="|\n0"
for x in range(int(a)):
	for y in range(5-len(str(x+1))):
		m+=" "
	m+=str(x+1)
	
print(m)


# 3.6
print("\nZADANIE 3.6")
a = 3  #wysokosc
b = 3  #dlugosc
 
l1=""
for x in range(a):
	for y in range(b):
		l1+="+---"
	l1+="+\n"
	for y in range(b):
		l1+="|   "
	l1+="|\n"
for x in range(b):
		l1+="+---"
l1+="+\n"
print(l1)



#3.8

print("\nZADANIE 3.8")
s1 = ["www","1",3,"yee",1]
s2 = ["d", "b","z", 13,1]
print("Elementy w obu sekwencjach: ", set(s1).intersection(set(s2) ))
print("Elementy obu sekwencji: ", set(s1+s2))
 

#3.9
print("\nZADANIE 3.9")
S = [[],[4],(1,2),[3,4],(5,6,7)]
Sr = []
for x in S:
	r = sum(x)
	Sr.append(r)
print(Sr)

#3.10

#tworzenie slownika
#standardowe
#slownik = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
#krotki
#slownik = [('M', 1000),('CM', 900),('D', 500),('CD', 400),('C', 100),('XC', 90),('L', 50),('XL', 40),('X', 10),('IX', 9),('V', 5),('IV', 4),('I', 1)]

slownik =  {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}

def roman2int(romanX):
	X = romanX.upper()
	result=0
	
	while X:
		if X[:2] in slownik:
			result+=slownik[X[:2]]
			X=X[2:]
		elif X[:1] in slownik:
			result+=slownik[X[:1]]
			X=X[1:]
		else:
			print("Podana liczba jest niepoprawna!")
			return
	print(result)
totranslate = input("Podaj liczbe w systemie rzymskim: ")
roman2int(totranslate)
