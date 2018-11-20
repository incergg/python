class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
             raise ValueError("Wartość mianownika równa 0!!!")
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x) 
        return (str(self.x) + "/" +str(self.y))
		
    def __repr__(self):        # zwraca "Frac(x, y)"
        return ("Frac("+str(self.x)+", " + str(self.y) + ")")
		
    def __add__(self, other):  # frac1+frac2, frac+int
        if isinstance(other, int):
             return Frac(self.x + other * self.y, self.y)
        if other.y == self.y:
             return Frac(self.x + other.x, self.y)
        return Frac( (self.x * other.y)+(other.x*self.y), (self.y * other.y))

    __radd__ = __add__              # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if isinstance(other, int):
             return Frac(self.x - (other * self.y), self.y)
        if other.y == self.y:
             return Frac(self.x - other.x, self.y)
        return Frac( (self.x * other.y)+(other.x*self.y), (self.y * other.y))
        
    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other, int):
            return Frac(self.x *other, self.y)
        return Frac(self.x * other.x, self.y*other.y)
		
    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other):  # frac1/frac2, frac/int
        if isinstance(other, int):
            if other == 0:
                raise ValueError ("Dzielenie przez 0!!!")
            return Frac(self.x , self.y * other)
        if other.x == 0:
            raise ValueError ("Dzielenie przez 0!!!")
        return Frac(self.x * other.y, self.y*other.x)
        
    def __rtruediv__(self, other): # int/frac
        if self.x == 0:
            raise ValueError("Dzielenie przez 0!!!")
        return Frac(other * self.y, self.x)
		
    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac((-1)*self.x,self.y)
    def __invert__(self):       # odwrotnosc: ~frac
         return Frac(self.y,self.x)
    def __float__(self):        # float(frac)
        return float(self.x)/float(self.y)
