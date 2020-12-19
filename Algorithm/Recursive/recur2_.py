# n이 홀수이면 3*n+1
# n이 짝수이면 n/2

def recur(n: int):
    print(n)
    if n==1:
        return n
    if n%2==1:
        return recur(3*n+1)
    else:
        return recur(n//2)

recur(3)