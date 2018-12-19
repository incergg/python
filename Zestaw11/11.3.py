def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0


def insertsort(L, left, right, cmpfunc=cmp):
    for i in range(right, left, -1): 
        if cmpfunc(L[i-1],L[i]): 
            L[i-1],L[i] = L[i],L[i-1]
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:
            L[j] = L[j-1]
            j = j-1
        L[j] = item
		
		
