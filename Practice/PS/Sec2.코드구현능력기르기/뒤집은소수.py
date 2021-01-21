# for i in range(1,6):
#     f1 = open('./PS/source/in{}.txt'.format(i), 'r')
    
#     n = int(f1.readline())
#     lt = list(map(int, f1.readline().split()))

#     def reverse(x):
#         s = str(x)
#         return int(s[::-1])

#     def isPrime(n):
#         if n==1:
#             return False
#         for i in range(2, n//2+1):
#             if n%i==0:
#                 return False
#         return True

#     for x in lt:
#         n = reverse(x)
#         if isPrime(n):
#             print(n, end=' ')
    
#     print()

    
n = 5
lt = {32, 55, 62, 3700, 250}

def reverse(x):
    s = str(x)
    return int(s[::-1])

def isPrime(n):
    if n==1:
        return False
    for i in range(2, n//2+1):
        if n%i==0:
            return False
    return True

for x in lt:
    n = reverse(x)
    if isPrime(n):
        print(n, end=' ')