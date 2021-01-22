def hanoi(n, from_, by, to):
    if n==1:
        print("%d %d"%(from_, to))
    else:
        hanoi(n-1, from_, to, by)
        print("%d %d"%(from_, to))
        hanoi(n-1, by, from_, to)
n = int(input())
print(2**n-1)
if n<20:
    hanoi(n, 1,2,3)