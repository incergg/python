import math
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		a = str(self.x)
		b = str(self.y)
		return ("("+a+", "+b+")")
		
	def __repr__(self): 
		a = str(self.x)
		b = str(self.y)
		return ("Point("+a+", "+b+")")
		
	def __eq__(self,other):
		if(self.x==other.x):
			if(self.y==other.y):
				return True
		return False	
	
	def __ne__(self,other):
		if(self.x==other.x):
			if(self.y==other.y):
				return False
		return True	
	
	def __add__(self,other):
		return  (Point(self.x+other.x,self.y+other.y))
	
	def __sub__(self,other):
		return  (Point(self.x-other.x,self.y-other.y))
	
	def __mul__(self,other):
		return ((self.x * other.x) +  (self.y*other.y))
		
	def cross(self,other):
		return (self.x*other.y-self.y*other.x)
		
	def length(self):
		return (math.sqrt(pow(self.x,2)+pow(self.y,2)))
		