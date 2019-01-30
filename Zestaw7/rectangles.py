from points import Point

class Rectangle:
	"""Klasa reprezentująca prostokąt na płaszczyźnie."""
	
	def __init__(self, x1, y1, x2, y2):
		if x1>x2 or y1>y2:
			raise ValueError("Punkty powinny wskazywać lewny dolny i prawy górny róg!!!") 
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)
	
	def __str__(self):         # "[(x1, y1), (x2, y2)]"
		return("[("+str(self.pt1.x)+", "+str(self.pt1.y)+"), ("+str(self.pt2.x)+", "+str(self.pt2.y)+")]")
		
	def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
		return("Rectangle("+str(self.pt1.x)+", "+str(self.pt1.y)+", "+str(self.pt2.x)+", "+str(self.pt2.y)+")")
	
	def __eq__(self, other):   # obsługa rect1 == rect2
		if(self.pt1.x==other.pt1.x):
			if(self.pt1.y==other.pt1.y):
				if(self.pt2.x==other.pt2.x):
					if(self.pt2.y==other.pt2.y):
						return True
		return False
		
	def __ne__(self, other):      # obsługa rect1 != rect2
		return not self == other
	
	def center(self):        # zwraca środek prostokąta
		return Point(((self.pt2.x+self.pt1.x)/2 ),((self.pt2.y+self.pt1.y)/2))
		
	def area(self):             # pole powierzchni
		return ((self.pt2.x-self.pt1.x)*(self.pt2.y-self.pt1.y))
		
	def move(self, x, y):       # przesunięcie o (x, y)
		return Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y)

	def intersection(self, other):
		if self.pt1.x < other.pt2.x:
			if self.pt2.x > other.pt1.x:
				if self.pt2.y > other.pt1.y:
					if self.pt1.y < other.pt2.y:
						p1x = max(self.pt1.x, other.pt1.x)
						p1y = max(self.pt1.y, other.pt1.y)
						p2x = min(self.pt2.x, other.pt2.x)
						p2y = min(self.pt2.y, other.pt2.y)
						return Rectangle(p1x,p1y,p2x,p2y)		
		return Rectangle(0,0,0,0)
		
	def cover(self, other):
		p1x = min(self.pt1.x, other.pt1.x)
		p1y = min(self.pt1.y, other.pt1.y)
		p2x = max(self.pt2.x, other.pt2.x)
		p2y = max(self.pt2.y, other.pt2.y)
		return Rectangle(p1x,p1y,p2x,p2y)
		
	def make4(self):
		r = []
		sx = (self.pt1.x+self.pt2.x)/2
		sy = (self.pt1.y+self.pt2.y)/2
		r.append(Rectangle(self.pt1.x,self.pt1.y,sx,sy))
		r.append(Rectangle(self.pt1.x,sy,sx,self.pt2.y))
		r.append(Rectangle(sx,sy,self.pt2.x,self.pt2.y))
		r.append(Rectangle(sx,self.pt1.y,self.pt2.x,sy))
		return r
	