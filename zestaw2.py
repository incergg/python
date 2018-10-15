
#2.10
line = "hello from\tthe otGvRher\n side gvr"
y=line.split()
print(len(y))

#2.11
word="word"
for x in range(0,len(word)-1):
	print(word[x], end='_')
print(word[len(word)-1])

#2.12
p=""
temp = line.split()
for x in range(0,len(temp)):
	p+=temp[x][0]
print(p)

k=""
for x in range(0,len(temp)):
	k+=temp[x][len(temp[x])-1]
print(k)
	

#2.13

temp = line.split();
print (sum([len(x) for x in temp]))


#2.14
l=""
temp =line.split()
for x in range(0,len(temp)):
	if len(temp[x]) > len(l):
		l=temp[x]
	
print(l, len(l))


#2.15
L=[12,23,53,32,12,2]
napis=""
for x in L:
	napis+=str(x)
print(napis)

#2.16
print(line)
line2=line.replace("GvR","Guid van Rossum")
print(line2)

#2.17
temp=line.split()
print(temp)
print(sorted(temp))
print(sorted(temp,key=len))
#2.18
o=10000320430341413405012300103424001230501230405000
ow=str(o)
i0=ow.count("0")
print(i0)

#2.19
napis=""
L=[12,23,53,32,12,2,123,64,753,1,54,434,123]
LW=str(L)
for x in range(0,len(L)):
	temp=str(L[x])
	napis+=temp.zfill(3)
	napis+=" "
print(napis)


#2.19
print('Zad 2.19\n')
L = [12, 1, 2, 3, 345, 3, 45, 243]
print (L)
Lstr = [str(x).zfill(3) for x in L]
print (", ".join(x for x in Lstr))
