
S = {(0,0):0.5}

def P(i,j):
	global S
	if (i,j) not in S:
		if j == 0:
			if i<=0:
				raise ValueError("j rowne 0, i nie wieksze od 0!")
			S[(i,j)] = 0.0
		elif i == 0:
			if j<=0:
				raise ValueError("'i' rowne 0, 'j' nie wieksze od 0!")
			S[(i,j)] = 1.0
		elif i>0 and j>0:
			S[(i,j)] = 0.5 * (P(i-1, j) + P(i, j-1))
		elif i<0 and j<0:
			raise ValueError("'i' oraz 'j' mniejsze od 0!")
	return S[(i,j)]


print(P(0,0))
print(P(1,0))
print(P(0,1))
print(P(3,4))
print(P(-1,-1))
