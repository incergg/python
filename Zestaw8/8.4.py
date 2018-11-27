import math
def heron(a, b, c):
	abc= [a,b,c]
	abc.sort()
	if abc[2]>=abc[0]+abc[1]:
		raise ValueError("Podane dlugosci nie tworza trojkata!")
	s = (a+b+c)/2
	A = math.sqrt(s*(s-a)*(s-b)*(s-c))
	return A
	
print ("{:.4f}".format(heron (3,3,4)))