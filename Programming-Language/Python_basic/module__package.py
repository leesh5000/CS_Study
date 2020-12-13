# section08
# 파이썬 모듈과 패키지

# 패키지
# 상대경로
# - .. : 상위 디렉토리
# - . : 현재 디렉토리

# 사용1
from pkg_Test.fibonacci import Fibo
Fibo.fib1(300)
print(Fibo.fib2(300))
print(Fibo().title)

# 사용2
# from pkg_Test.fibonacci import *

# 사용3 (alias)
from pkg_Test.fibonacci import Fibo as fb
print(fb.fib2(1000))

# 사용4 (함수가져오기)
import pkg_Test.cal as c
print(c.add(1,10))

# 사용5 (필요한 함수만 가져오기)
from pkg_Test.cal import add as a
print(a(1,10))

# 예제
import pkg_Test.prints as p
import builtins # 파이썬 stl
p.prt1()
p.prt2()
print(dir(builtins))