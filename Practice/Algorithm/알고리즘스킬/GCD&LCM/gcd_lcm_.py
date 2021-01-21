# Greatest Common Divisor
# - 유클리드 호제법
# 1. 최대공약수 함수를 gcd(a,b)라고 하자.
# 2. a mod b = 0 이라면, gcd(a,b) = b가 성립
# 3. a mod b != 0 이라면, gcd(a,b) = gcd(b, a mod b)

# Least Common Multipl
# 최소공배수
# LCM(a,b) = (a*b) / GCD(a,b)

# N개의 수에 대한 최소공배수

def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a,b)

print(gcd(1071,1029))
print(lcm(1071,1029))

# 예제. n개의 수에 대해서 gcm, lcm 구하기
# 입력예제
# 3
# 4 6 8
# 출력예제
# 2 48

n = int(input())
lt = []
while n:
    lt.append(int(input()))
    n -= 1

ans = []
gcd_ans = 0
for i in range(len(lt)-1):
    gcd(lt[i], lt[i+1])
