# 자릿수의 합
# - 자릿수의 합 중요!

for i in range(1,6):
    f1 = open('./PS/source/in{}.txt'.format(i), 'r')
    
    n = int(f1.readline())
    lt = list(map(int, f1.readline().split()))

    # 자릿수의 합 함수
    def digit_sum(x):
        sum = 0
        while x > 0:
            sum += x % 10
            x = int(x/10)
        return sum
    
    # Pythonic
    def digit_sum_pythonic(x):
        sum = 0
        for i in str(x):
            sum += int(i)

    max = -2147000000
    for x in lt:
        tot = digit_sum(x)
        if tot > max:
            max = tot
            ans = x
        
    print(ans)