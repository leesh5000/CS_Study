# 파이썬은 함수 오버로딩을 지원하지 않음
# 하지만, 비슷한 것으로 매개변수 *args, **kwargs로 함수의 다형성을 보장할 수 있음

# 1. *args: 가변인자
# - 인자를 튜플로 받아줌
# - 매개변수가 몇 개가 될 지 모를때 사용
# - 매개변수에 따라 함수의 작동을 달리하고 싶을때 사용

def args(*args):
    print(args)

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