def reverse(n):
    res = 0
    while n > 0:
        t = n % 10
        res = res * 10 + t
        n = n // 10
    return res

print(reverse(9010))