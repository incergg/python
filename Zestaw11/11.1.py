import math
import random

def randomlist(N):
	numbers = []
	for i in range(0,N):	
		numbers.append(random.randint(0,N-1))
	return numbers
	
def nearlysortedlist(N):
	numbers = []
	if N>100:
		x = (int)(N/18)
	elif N>=10:
		x = 6
	else:
		x=3
	for i in range(1,N):
		if i%x==0:
			numbers.append(random.randint(0,N-1))
		else:
			numbers.append(i)
	return numbers
		


def reversednsorted(N):
	numbers = nearlysortedlist(N)
	numbers.reverse()
	return numbers
	


def floatGauss(N, mu, sigma): 
	numbers = []
	for i in range(1,N):
		numbers.append(random.gauss(mu, sigma))
	return numbers

def zbior(N):
	numbers = []
	for i in range(0, N):
		numbers.append(random.randint(0, int(math.sqrt(N))))
	return numbers

