# 전체적인 파이썬 기능 개괄

import this  # 파이썬 코딩 철학
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 변수 선언
myName = 'SH'

# 조건문
if myName == 'SH':
    print('Right')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)

# 함수


def Greeting():
    print("HI, Hello")


Greeting()

# 클래스


class Cookie:
    pass


# 인스턴스(객체생성)
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
