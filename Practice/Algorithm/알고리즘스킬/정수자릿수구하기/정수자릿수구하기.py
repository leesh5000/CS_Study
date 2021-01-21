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
