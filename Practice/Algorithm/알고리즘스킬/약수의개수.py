def divisor_cnt(n):
    # 1과 자기자신
    cnt = 2
    # n/2~n까지에서는 n의 약수가 존재할 수 없다.
    for i in range(2, n//2+1):
        if n % i == 0:
            cnt += 1
    return cnt

print(divisor_cnt(28))


