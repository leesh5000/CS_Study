# section06-1
# 하나의 함수에 하나의 기능만

# 1.
def Hello(word):
    print("Hello", word)

Hello("python")

# 2.
def sum_int(a, b):
    return a+b

print(sum_int(4,6))

# 3. 다중리턴
def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1,y2,y3

val1, val2, val3 = func_mul(5)
print(val1, val2, val3)

# 4. 데이터타입 반환
def func_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1,y2,y3]

lt = func_mul2(5)
print(lt)

# 5. *args : 가변인자
# - 인자를 튜플로 받아줌
# - 매개변수가 몇 개가 될지 모를때
# - 또는, 매개변수에 따라 함수의 작동을 달리할때

def args_func(*args):
    print(type(args), args)

args_func('kim')
args_func('kim', 'lee', 'park')

def args_func1(*args):
    for i,v in enumerate(args):
        print(type(i), type(v), i, v)

args_func1('kim')
args_func1('kim', 'lee', 'park')

# 6. *kwargs 인자
# - *가 하나이면 튜플
# - *가 두개이면 딕셔너리

def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='kim', name2='lee', name3='park')

def kwargs_func1(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

kwargs_func1(name1='kim', name2='lee', name3='park')

# 예제1

# arg1,arg2는 필수인자, *args는 튜플을 받는 가변인자, **kwargs는 딕셔너리를 받는 가변인자
def ex_fun1(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

ex_fun1(10,20)
ex_fun1(10,20,30,40)
ex_fun1(10, 20, 'lee', 'kim', age1=27, age2=24)

# 7. 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 6. 힌트
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

# 람다식 예제
# 장점 : 메모리절약, 가독성 향상
# 함수는 객체생성 -> 메모리 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리초기화

# 일반함수 -> 변수할당
def mul_10(num:int)->int:
    return num*10

var_func = mul_10
print(var_func)
print(mul_10)
print(type(var_func))

print(var_func(10))

# 람다이름 = lambda 입력 : 출력
lambda_mul_10 = lambda num : num*10

print(lambda_mul_10(10))

def func1(x, y, func):
    print(x*y*func(10))

func1(10,10,lambda_mul_10)
func1(10,10,lambda num:num*10)