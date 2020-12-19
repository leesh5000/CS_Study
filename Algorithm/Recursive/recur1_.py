# 1부터 n까지의 곱
def mul(n):
    if (n==1):
        return 1
    else:
        return n * mul(n-1)

print(mul(10))


