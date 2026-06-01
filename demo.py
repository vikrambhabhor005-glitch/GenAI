def highest(l1,n):
    l1.sort(reverse=True)
    return l1[n-1]
print(highest([1,3,5,7,2,4,6,8,],3))