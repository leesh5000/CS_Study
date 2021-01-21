# 피보나치
# 1. DP
# 2. Divide and Conquer

def fibo_dp(n):
    memo = [0 for i in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fibo_dc(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo_dc(n-1) + fibo_dc(n-2)

print(fibo_dc(8))
print(fibo_dp(8))