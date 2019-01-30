def cmp(a, b):
	if a > b:
		return 1
	elif a < b:
		return -1
	return 0
	
	
def insertsort(L, left=0, right=0, cmpfunc=cmp):
	if right == 0:
		right = len(L)-1
	for i in range(right, left, -1): 
		if cmpfunc(L[i-1],L[i]) > 0: 
			L[i-1],L[i] = L[i],L[i-1]
	for i in range(left+2, right+1):
		j = i
		item = L[i]
		while cmpfunc(item, L[j-1]) < 0:
			L[j] = L[j-1]
			j = j-1
		L[j] = item
	
	
L1 = [6,1,3,3,2,5,1,7,0]
L2 = [4,2,3,6,1,2,8,5,9]

insertsort(L1)
insertsort (L2,0,6)


print(L1,"\n",L2)