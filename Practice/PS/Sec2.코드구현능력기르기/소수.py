# 에라토스테네스의 체
# 많은 소수 구하는 방법 중 가장 빠른 방법

def eratos(n):
    lt = [True] * (n+1)
    cnt = 0
    for i in range(2, n+1):
        if lt[i]==True:
            cnt += 1
            for j in range(i+i, n+1, i):
                lt[j] = False
    print(cnt)

eratos(2)

