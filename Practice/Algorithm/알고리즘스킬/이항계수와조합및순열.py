def factorial(k):
    if k < 1:
        return 1
    else:
        return k * factorial(k-1)
def permutation(n,k):
    return factorial(n) // factorial(n-k)
def combination(n,k):
    return permutation(n,k) // factorial(k)
def binomal(n):
    bi = []
    if n==0:
        return bi
    if n==1:
        return bi.append(1)        
    for i in range(n):
        bi.append(combination(n-1,i))
    return bi