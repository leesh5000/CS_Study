## 재귀용법으로 구현
def fibo_recur(n: int)->int:
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_recur(n-1)+fibo_recur(n-2)

print(fibo_recur(4))

## DP로 구현
def fibo_dp(n: int)->int:
    fibo = [0 for i in range(n+1)]
    fibo[0]=0
    fibo[1]=1

    for i in range(2, n+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
    
    return fibo[n]

print(fibo_dp(4))