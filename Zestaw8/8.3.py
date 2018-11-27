import random
import math


def calc_pi(n=100):
	inrange=0
	min=100
	max=0
	result=0
	avg=0
	for y in range(100):
		inrange=0
		result=0
		for x in range(n):
			a=random.random()
			b=random.random()
			if math.sqrt((pow(a,2)+pow(b,2))) < 1:
				inrange+=1
		result = 4*inrange/n
		avg+=result
		if result>max:
			max = result
		if result<min:
			min = result
	print ( "\n Ostatnie losowanie: " + "{:.2f}".format(result) + "\n\n Statystyki 100 losowan po " + str(n) + " punktow:\n Srednia: "+ "{:.2f}".format(avg/100) + " Maksimum: " +"{:.2f}".format(max) +" Minimum: " + "{:.2f}".format(min) +"\n")
	return avg/100	
calc_pi(50)
calc_pi(100)
calc_pi(1000)
calc_pi(10000)
calc_pi(40000)