def solve1(a, b, c):
	if a==0:
		if b==0:
			if c==0:
				return ( "Nieskonczenie wiele rozwiazan!")
			return ("Brak rozwiazan!")
		return ("y= {:.2f}".format(-c/b)+"\n")
			
	if b==0:
		return ("x= {:.2f}".format(-c/a))
		
	return ("y= {:.2f}".format(-a/b)+"x + {:.2f}".format(-c/b)  )
			
			
print (solve1(5,3,2))