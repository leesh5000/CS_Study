## Programmin Language

## Contents

- [Python](#python)
  - [파이썬의 장점](#파이썬의-장점)
  - [기본출력](#기본출력)
  - [파이썬의 데이터타입](#파이썬의-데이터타입)
    1. [기본자료형](#1-기본자료형)
    2. [문자열](#2-문자열)
    3. [리스트](#3-리스트)
    4. [튜플](#4-튜플)
    5. [딕셔너리](#5-딕셔너리)
    6. [집합](#6-집합)
  - [코드의 흐름제어](#코드의-흐름제어)
    1. [조건문](#1-조건문)
    2. [반복문](#2-반복문)
  - [함수](#함수)
    1. [기본문법](#1-기본문법)
    2. [*args,**kwargs](#2-args-kwargs)
    3. [중첩함수](#3-중첩함수클로저)
    4. [힌트](#4-힌트)
    5. [람다식](#5-람다식)
  - [클래스](#클래스)
    1. [기본문법](#1-기본문법)
    2. [클래스매소드와 인스턴스매소드](#2-클래스매소드와-인스턴스매소드)
    3. [클래스변수와 인스턴스변수](#3-클래스변수-인스턴스변수self)
    4. [상속](#4-상속)
    5. [오버라이딩](#5-오버라이딩)
    6. [다중상속](#6-다중상속)
  - [모듈과 패키지](#모듈과-패키지)
  - [파일 I/O](#파일-IO)
  - [예외처리](#예외처리)
  - [외부파일처리](#파이썬-외부파일-처리)
    1. [CSV](#1-csv)
    2. [Excel](#2-excel-읽기쓰기)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

# Python

## 파이썬의 장점
- 사용하기 쉽다.
- 파이썬 인터프리터만 있으면 어느 운영체제든지 실행가능하다.
- 다양한 라이브러리가 존재한다.
- 과학, 머신러닝, 웹 등 범용적으로 사용된다.

<br>[Contents](#Contents)<br><br>

## 기본출력

#### 기본문법
```
print('Hello Python!')
-> Hello Python!

print("Hello Python!")
-> Hello Python!

print("""Hello Python!""")
-> Hello Python!

print('''Hello Python!''')
-> Hello Python!
```

#### 줄바꿈
```
print()
-> 
```

#### Seperate 옵션 사용
```
print('T', 'E', 'S', 'T', sep='')
-> TEST

print('2020','09','07', sep='-')
-> 2020-09-07

print('lsh','google.com', sep='@')
-> lsh@google.com
```


#### End 옵션 사용
```
print('Hi', end=' Python')
-> Hi Python

print('\nPython is ', end='Good\n')
-> Python is Good
```

#### format 옵션 사용
```
print('{} and {}'.format(1,2))
-> 1 and 2

print("{0} and {1} and {0}".format('zero','one'))
-> zero and one and zero

print("{a} are {b}".format(a='You', b='Me'))
-> You are Me

print("%s's favorite number is %d" % ('SH', 7))
-> SH's favorite number is 7

print("Test1 : %5d, Price : %4.2f" % (101, 1234.56789))
-> Test1 :   101, Price : 1234.57

print("Test2 : {0: 5d}, Price : {1: 4.2f}".format(101,1234.567))
-> Test2 :   101, Price :  1234.57

print("Test3 : {a: 5d}, Price : {b: 4.2f}".format(a=101,b=1234.567))
-> Test3 :   101, Price :  1234.57
```

#### Escape 코드
```
print("'you'")
-> 'you'

print('"Hi"')
-> "Hi"

print('\'Hello\'')
-> 'Hello'

print('\\Python\\')
-> \pytonh\

print('\\n\n')
-> \n

print('\ttap')
->    tap
```

<br>[Contents](#Contents)<br><br>

## 파이썬의 데이터타입
- Boolean
- Numbers
- String
- Bytes
- Lists
- Tuples
- Sets
- Dictionaries


## 1. 기본자료형
```
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7]

print(type(v_tuple))
-> <class 'tuple'>

print(type(v_set))
-> <class 'set'>

print(type(v_float))
-> <class 'float'>
```

#### 형 변환
```
a = 5.
b = 10

print(type(a), type(b))
-> 5. 10

result2 = a+b
print(result2) 
-> 15.0

print(int(result2))
-> 15

print(int('3'))
-> 3
```

#### 연산
```
i1 = 39
i2 = 939
big_int1 = 9999999999999999999991293810
big_int2 = 1092810724129040124801294817
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1*i2)
print(big_int1 * big_int2)
print(f1 ** f2)

result = f3 + i2
print(result, type(result))
```

#### 수치 연산 관련 함수
```
print(abs(-7))
n, m = divmod(100, 8) 
-> n = quotient , m = remainder

import math ## 수학관련 모듈 
print(math.ceil(5.1)) # 5.1보다 크면서 가장 작은 정수
-> 6

print(math.floor(3.874)) # 3.874보다 작으면서 가장 큰 정수
-> 3
```

<br>[Contents](#Contents)<br><br>

## 2. 문자열
```
str1 = "I am Boy."
str2 = "NiceMan"
str3 = ' '

print(len(str1), len(str2), len(str3))
-> 9,7,1 출력

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
-> Do you have a big collection

escape_str2 = "Tab\tTab"
print(escape_str2)
-> Tab     Tab
```

#### Raw String
```
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
-> C:\Programs\Test\Bin

raw_s2 = r"\n\t''"
print(raw_s2)
-> \n\t''
```

#### 멀티라인
```
multi = \
""" 
string 
multiline 
test 
"""

print(multi)
->
'''
string 
multiline 
test 
'''
```

#### 문자열 연산
```
str_o1 = "*"
str_o2 = 'abc'
str_o3 = 'def'

print(str_o1 * 30)
-> ******************************

print(str_o3 + str_o2)
-> defabc

str_o4 = "Niceman" # ""는 immutable로 한번 할당되면 수정이 불가능한 시퀀스. 순회가 가능하다.
print('a' in str_o4)
-> immutable은 순회가 가능

print('z' not in str_o4)
-> True
```

#### 문자열 형변환
```
print(str(77) + 'a') 
-> 77a
```

#### 문자열 관련 함수
```
a = "niceman"
b = "orange"

print(a.islower())
-> True

print(b.endswith('e'))
-> True

print(a.capitalize())
-> Niceman

print(a.replace('nice','good'))
-> goodman

print(list(reversed(b)))
-> ['e', 'g', 'n', 'a', 'r', 'o']
```

#### 문자열 슬라이싱
- 파이썬에서 immutable은 변경불가능한 자료형을 말한다.
- 문자열이 각각의 인덱스를 갖고 있기 때문에 파이썬에서 문자열은 immutable이다.

```
c = 'niceman'
d = 'orange'

print(c[0:3])
-> nic

print(c[0:len(c)])
-> niceman

print(c[:4])
-> nice

print(c[:])
-> niceman

print(d[0:4:2])
-> oa

print(d[1:-2])
-> ran

print(d[::-1])
-> egnaro
```

<br>[Contents](#Contents)<br><br>

## 3. 리스트
- 리스트(순서o, 중복o, 수정o, 삭제o)

#### 리스트 선언
```
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]
```

#### 리스트 인덱싱
```
print(d[3])
-> Banana

print(d[-2])
-> Banana

print(d[0]+d[1])
-> 110

print(e[2][1])
-> Banana

print(e[-1][-2])
-> Banana
```

#### 슬라이싱
```
print(d[0:3])
-> [10, 100, 'Pen']

print(e[2][1:3])
-> ['Banana', 'Orange']
```

#### 연산
```
print(c+d)
-> [1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']

print(c*3)
-> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

print(str(c[0])+'hi')
-> 1hi
```

#### 리스트 수정/삭제
```
c[0] = 77
print(c)
-> [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000] # 슬라이싱 처리를 하고 리스트를 넣으면
print(c)
-> [77, 100, 1000, 10000, 3, 4]

c[1] = [100, 1000, 10000] # 슬라이싱 처리를 하지 않고 리스트를 넣으면
print(c)
-> [77, [100, 1000, 10000], 1000, 10000, 3, 4]

del c[1]
print(c)
-> [77, 1000, 10000, 3, 4]

del c[-1]
print(c)
-> [77, 1000, 10000, 3]
```

#### 리스트 함수
```
y = [5, 2, 3, 1, 4]
print(y)
-> [5, 2, 3, 1, 4]

y.append(6)
print(y)
-> [5, 2, 3, 1, 4, 6]

y.sort()
print(y)
-> [1, 2, 3, 4, 5, 6]

y.reverse()
print(y)
-> [6, 5, 4, 3, 2, 1]

y.insert(2, 7)
print(y)
-> [6, 5, 7, 4, 3, 2, 1]

y.remove(2) # remove는 값에 해당하는 원소를 삭제
print(y)
-> [6, 5, 7, 4, 3, 1]

y.pop()
print(y)
-> [6, 5, 7, 4, 3]

ex = [88, 77]
y.extend(ex)
y.append(ex)
print(y)
-> [6, 5, 7, 4, 3, 88, 77, [88, 77]]
```

#### list comprehension

```
lt1 = []
for n in range(1,101):
    lt1.append(n)
print(lt1)

lt2 = [x for x in range(1,101)]
print(lt2)

q3 = ["a", "b", "c", "d"]
lt3 = [x for x in q3 if x != "b"]
print(lt3)

q6 = [x for x in range(1,101) if x%2 != 0]
print(q6)
```

<br>[Contents](#Contents)<br><br>

## 4. 튜플
- 튜플(순서o, 중복o, 수정x, 삭제x)
- 변경되면 안되는 중요한 값이 저장되는 곳에 쓰임

#### 튜플의 선언
```
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
e = tuple()
```

#### 튜플 인덱싱
```
print(c[2])
-> 3

print(d[2][1])
-> b
```

#### 튜플 슬라이싱
```
print(d[2:])
-> (('a', 'b', 'c'),)

print(d[2][0:2])
-> ('a', 'b')
```

#### 연산
```
print(c+d)
-> (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))

print(c*3)
-> (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

```

#### 튜플함수
```
e = (5,2,1,3,4,1)
print(e)
-> (5, 2, 1, 3, 4, 1)

print(3 in e)
-> True

print(e.index(5))
-> 0

print(e.count(1))
-> 2
```

<br>[Contents](#Contents)<br><br>

## 5. 딕셔너리
- 딕셔너리는 순서x, 중복x(key만), 수정o, 삭제o
- 딕셔너리는 웹 브라우저 데이터 송신에 사용되는 Json 형식과 비슷

#### 선언
```
a = {'name': 'Lee', 'phone': '010-0000-0000', 'address': '12345'}
b = {0: 'Hello Python', 1: 'Hello Java'}
c = {'arr': [1,2,3,4,5], 'tuple': (1,2,3,4,5,)}

print(type(a))
-> <class 'dict'>

print(a['name'])
-> Lee

print(a.get('name'))
-> Lee

print(a.get('birth'))
-> None

print(c['arr'][1:3])
-> [2, 3]
```

#### 딕셔너리 추가
```
a['birth'] = '941008'
print(a)
-> {'name': 'Lee', 'phone': '010-0000-0000', 'address': '12345', 'birth': '941008'}

a['rank'] = [1,2,3]
a['rank2'] = (1,2,3,)
print(a)
-> {'name': 'Lee', 'phone': '010-0000-0000', 'address': '12345', 'birth': '941008', 'rank': [1, 2, 3], 'rank2': (1, 2, 3)}
```

#### keys, values, items
```
print(a.keys())
-> dict_keys(['name', 'phone', 'address', 'birth', 'rank', 'rank2'])

print(a.keys()[2])
-> 에러

print(list(a.keys())[1:3])
-> ['phone', 'address']

print(a.values())
-> dict_values(['Lee', '010-0000-0000', '12345', '941008', [1, 2, 3], (1, 2, 3)])

print(a.items())
-> dict_items([('name', 'Lee'), ('phone', '010-0000-0000'), ('address', '12345'), ('birth', '941008'), ('rank', [1, 2, 3]), ('rank2', (1, 2, 3))])

temp = list(a.items())
print(temp)
-> [('name', 'Lee'), ('phone', '010-0000-0000'), ('address', '12345'), ('birth', '941008'), ('rank', [1, 2, 3]), ('rank2', (1, 2, 3))]

print(2 in b)
-> False

print('name' in a)
-> True
```
<br>[Contents](#Contents)<br><br>

## 6. 집합
집합(set)은 순서x, 중복x
```
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 6, 6, 6])

print(type(a))
-> <class 'set'>

print(c)
-> {1, 4, 6}
```

#### set은 주로 변환을 해서 사용한다.
```
t = tuple(b)
print(t)
-> (1, 2, 3, 4)

l = list(b)
print(l)
-> (1, 2, 3, 4)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
-> {4, 5, 6}

print(s1 & s2)
-> {4, 5, 6}

print(s1.union(s2))
-> {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1 | s2)
-> {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1 - s2)
-> {1, 2, 3}

print(s1.difference(s2))
-> {1, 2, 3}
```

#### 추가/제거
```
s3 = set([7, 8, 9, 15])
s3.add(18)
s3.add(7)
print(s3)
-> {7, 8, 9, 15, 18}

s3.remove(15)
print(s3)
-> {7, 8, 9, 18}
```

<br>[Contents](#Contents)<br><br>

# 코드의 흐름제어

## 1. 조건문

#### 기본문법
```
print(type(True))
print(type(False))

if True:
    print("Yes")

if False:
    print("No")

if False:
    print("No")
else:
    print("Yes")

a = 10
b = 0

print(a==b)
print(a!=b)
print(a>=b)
```

#### True, False 종류
- True : "내용", [내용], (내용), {내용}, 1
- False : "", [], (), {}, 0
```
str_test = ""

if str_test:
    print("T")
else:
    print("F")
```

#### 논리연산자 : and, or, not
```
a = 100
b = 60
c = 15

print('and :', a>b and b>c)
print('or :', a>b or c>b)
print('not :', not a>b)
```

#### 연산자 우선순위
- 산술(+,-,..), 관계(>,=,<,..), 논리(and,or,not) 연산자 우선순위
- 산술 > 관계 > 논리
```
print('test : ', 5+10>0 and not 7+3==10)
```

#### 다중조건문
```
num = 100

if num>=90:
    print("A", num)
elif num >=80:
    print("B", num)
elif num >=70:
    print("C", num)
else:
    print("F", num)
```

<br>[Contents](#Contents)<br><br>

## 2. 반복문

#### for, while
```
v1 = 1
while v1 < 11:
    print("v1 is :",v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :",v2)

for v3 in range(1,10):
    print("v3 is :",v3)

sum1 = 0
for i in range(1,101):
    sum1 += i
print("1~100 합 :", sum1)
print("1~100 합 :", sum(range(1, 101)))
print("1~100 짝수합 :", sum(range(0, 101, 2)))
```

#### 시퀀스 자료형, 문자열, 리스트, 튜플, 집합, 사전은 반복가능
- iterable 리턴함수 : range, reversed, enumerate, filter, map, zip, ...
```
names = ["Lee", "Kim", "Park", "Yoo"]

for name in names:
    print("You are :", name)

word = "dreams"

for s in word:
    print("Word :",s)

my_info = {
    "name" : "kim",
    "age" : "33",
    "city" : "seoul"
}

for k in my_info:
    print("my_info :", k)

for k in my_info.keys():
    print("my_info :", k)

for v in my_info.values():
    print("my_info :", v)

for i in my_info.items():
    print("my_info :", i)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
```

#### for-else
```
numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if (i==17):
        print("Found : %d" % i)
        break
else:
    print("Not found 7")
```

#### 자료구조 변환
```
name = "helloC"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
```

<br>[Contents](#Contents)<br><br>

## 함수
- 하나의 함수에 하나의 기능만

## 1. 기본문법
```
def Hello(word):
    print("Hello", word)

Hello("python")

def sum_int(a, b):
    return a+b

print(sum_int(4,6))
```

#### 다중리턴
```
def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1,y2,y3

val1, val2, val3 = func_mul(5)
print(val1, val2, val3)
```

#### 데이터타입 반환
```
def func_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1,y2,y3]

lt = func_mul2(5)
print(lt)
```

## 2. *args, *kwargs

#### *args : 가변인자
- 인자를 튜플로 받아줌
- 매개변수가 몇 개가 될지 모를때
- 또는, 매개변수에 따라 함수의 작동을 달리할때

```
def args_func(*args):
    print(type(args), args)

args_func('kim')
args_func('kim', 'lee', 'park')

def args_func1(*args):
    for i,v in enumerate(args):
        print(type(i), type(v), i, v)

args_func1('kim')
args_func1('kim', 'lee', 'park')
```

#### *kwargs
- *가 하나이면 튜플
- *가 두개이면 딕셔너리

```
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
```

## 3. 중첩함수(클로저)
```
def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)
```

## 4. 힌트
```
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]
```

## 5. 람다식
- 장점 : 메모리절약, 가독성 향상
- 함수는 객체생성 -> 메모리 할당
- 람다는 즉시 실행(heap 초기화) -> 메모리초기화
```
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
``` 

<br>[Contents](#Contents)<br><br>

## 클래스

## 1. 기본문법
#### 선언
- __init__은 c언어의 생성자 같은 것
- self는 클래스의 인스턴스 변수
- 클래스 : 붕어빵 틀
- 객체 : 소프트웨어에서 구현할 실제대상
- 인스턴스 : 붕어빵, 객체를 메모리에 할당한 것

```
class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Class Initiated!")
    def Print_Info(self):
        print("Name : %s\nAge : %d\n" % (self.name, self.age))

user1 = UserInfo("LSH", 27)
user1.Print_Info()

user2 = UserInfo("KYJ", 24)
user2.Print_Info()
```

#### 클래스의 네임스페이스

```
print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)
```

## 2. 클래스매소드와 인스턴스매소드 
- 클래스매소드 : 클래스에서 직접사용 가능
- 인스턴스매소드 : 인스턴스마다 별도로 존재, 인스턴스 생성 후 사용

```
class SelfTest:
    # 클래스 매소드
    def func1():
        print('func1 called!')
    # 인스턴스 매소드
    def func2(self):
        print('func2 called!')
        print(id(self))

self_Test1 = SelfTest()
self_Test1.func2()
SelfTest.func1()

print(id(self_Test1))
SelfTest.func2(self_Test1)
```

## 3. 클래스변수 인스턴스변수(self)
- 클래스변수 : 모든 인스턴스 변수가 공유, 네임스페이스는 클래스명
- 인스턴스변수 : 인스턴스마다 별도로 존재, 네임스페이스는 인스턴스명

```
class Warehouse:
    # 클래스 변수, 각각 인스턴스 변수가 공유, static변수와 같은것?
    num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.num += 1
    def __del__(self):
        Warehouse.num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Kim')
user3 = Warehouse('Park')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(Warehouse.__dict__)

print(user1.num)
print(user2.num)
print(user3.num)

del user1

print(user2.num)
print(user3.num)
```

## 4. 상속
- 파이썬은 다중상속 지원
- 자바는 인터페이스 지원, 다중상속 지원x
- 코드의 재사용, 생산성 향상
- 부모클래스의 모든 속성,메소드 사용 가능
- 부모클래스 = 상위클래스 = 슈퍼클래스
- 자식클래스 = 하위클래스 = 서브클래스

```
class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def Show_Info(self) -> None:
        return 'Car Class "Show Method!"'

class BMW(Car):
    """Child Class"""
    def __init__(self, name, tp, color):
        super().__init__(tp, color)
        self.name = name
    
    def Show_Name(self) -> None:
        return "Your Car Name : %s" % self.name

car1 = BMW('520d', 'sedan', 'red')
print(car1.color)
print(car1.type)
print(car1.name)
print(car1.Show_Info())
print(car1.Show_Name())

print(car1.__dict__)
```

## 5. 오버라이딩

```
class Benz(Car):
    """Child Class"""
    def __init__(self, name, tp, color):
        super().__init__(tp, color)
        self.name = name
    
    def Show_Name(self) -> None:
        return "Your Car Name : %s" % self.name

    def Show_Info(self) -> None:
        print(super().Show_Info())
        return "Benz Overriding"

car2 = Benz('220d', 'suv', 'white')
print(car2.Show_Info())

# Inheritance Info
# - 상속 정보를 리스트 형태로 반환해주는 매소드
# - 왼쪽에서 오른쪽으로 상위 클래스 이름이 나옴
print(BMW.mro())
print(Benz.mro())
```

## 6. 다중상속

```
class X():
    pass

class Y():
    pass

class A(X,Y):
    pass

print(A.mro())
```

<br>[Contents](#Contents)<br><br>

## 모듈과 패키지
- .. : 상위 디렉토리
- . : 현재 디렉토리

#### 사용1
from pkg_Test.fibonacci import Fibo
Fibo.fib1(300)
print(Fibo.fib2(300))
print(Fibo().title)

#### 사용2
- from pkg_Test.fibonacci import *

#### 사용3 (alias)
from pkg_Test.fibonacci import Fibo as fb
print(fb.fib2(1000))

#### 사용4 (함수가져오기)
import pkg_Test.cal as c
print(c.add(1,10))

#### 사용5 (필요한 함수만 가져오기)
from pkg_Test.cal import add as a
print(a(1,10))

#### 예제
import pkg_Test.prints as p
import builtins # 파이썬 stl
p.prt1()
p.prt2()
print(dir(builtins))

<br>[Contents](#Contents)<br><br>

## 파일 I/O
- 읽기모드 : r
- 쓰기모드(덮어쓰기) : w
- 추가모드 : a

## 1. 파일 읽기

#### 파일읽기1

```
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
f.close()
```

#### 파일읽기2
- with는 close를 안해도 자동으로 close 해준다.

```
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
```

#### 파일읽기3

```
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())
```

#### 파일읽기4 
- 한번 read를 하면 커서가 파일 끝으로 가서 더 읽을게 없음

```
with open('./resource/review.txt', 'r') as f:
    contents1 = f.read()
    contents2 = f.read()
    print("c1>>", contents1)
    print("c2>>", contents2)
```

#### 파일읽기5
- 한줄씩 읽어오기

```
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    print(line)
    while line:
        print(line, end=' #### ')
        line = f.readline()
```

#### 파일읽기6
- readlines는 list를 반환

```
with open('./resource/review.txt', 'r') as f:
    c1 = f.readlines()
    print(c1)
    for c in c1:
        print(c, end= ' #### ')


print('\n\n')
```

#### 예제
- score파일 읽어서 평균내기

``` 
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Average : {:6.3}".format(sum(score)/len(score)))
```

## 2. 파일 쓰기

#### 파일쓰기1

```
with open('./resource/text1.txt', 'w') as f:
    f.write("Nice man!\n")

with open('./resource/text1.txt', 'a') as f:
    f.write("Good man!\n")
```

#### 파일쓰기2

```
from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')
```

#### 파일쓰기3 
- 리스트형태를 파일로 쓰기

```
with open('./resource/text3.txt', 'w') as f:
    list = ['lee\n', 'kim\n', 'park\n']
    f.writelines(list)
```

#### 파일쓰기4
- print문으로 파일쓰기

```
with open('./resource/text2.txt', 'w') as f:
    print('Test1', file=f)
    print('Test2', file=f)
```

<br>[Contents](#Contents)<br><br>

## 예외처리
- linter : 코드 스타일, 문법 체크

## 1. SyntaxError : 문법이 틀린 경우
```
 if True
     pass
```

## 2. NameError : 참조변수가 없을때
```
a = 10
b = 15
print(c)
```
## 3. ZeroDivisionError : 0 나누기 에러
```
 print(10/0)
```

## 4. IndexError : 인덱스 범위 오버
```
 x = [10, 20, 30]
 print(x[4])
```

## 5. KeyError
```
 dic = {'name': 'kim'}
 print(dic['hobby'])
 print(dic.get('hobby'))
```
## 6. AttributeError : 모듈, 클래스에 잘못된 속성 사용 시 예외
```
 class Test:
     val1
     val2
 t = Test()
 t.val3
```
## 7. ValueError : 참조값이 없을 때 발생
```
 x = [1, 5, 9]
 x.remove(10)
 x.index(10)
```

## 8. FileNotFoundError
```
 f = open('test.txt', 'r')
```

## 9. TypeError
```
 x = [1, 2]
 y = (1, 2)
 print(x+y)
```

## EAFP 코딩 스타일
- 1. 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
- 2. 그 후 런타임 예외 발생시 예외처리 하기

## 예외처리 기본

### 1. try
- 예외가 발생할 가능성이 있는 코드 실행
- 예외가 발생하면 except문으로 이동

### 2. except
- 예외가 발생할 경우 실행

### 3. else
- 예외가 발생하지 않은 경우 실행

### 4. finally
- 항상 실행되는 구문

### 5. 예외처리1 - 예외가 예상될때
```
name = ['lee', 'kim', 'park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} found it! in name'.format(z))
except ValueError:
    print('not found it! - valueError')
else:
    print('ok!')
```

### 예외처리2 - 어떤 예외가 발생할지 모를때
```
 name = ['lee', 'kim', 'park']

 try:
     z = 'kim'
     x = name.index(z)
     print('{} found it! in name'.format(z))
 except Exception:
     print('not found it!')
 else:
     print('ok!')
```

### 예외처리3 - finally
```
 name = ['lee', 'kim', 'park']

 try:
     z = 'kim'
     x = name.index(z)
     print('{} found it! in name'.format(z))
 except Exception:
     print('not found it!')
 else:
     print('else')
 finally:
     print('finally')
```

### 예외처리4 - 예외처리는 하지 않지만 무조건 수행되는 코딩패턴
```
 try:
     print('Try')
 finally:
     print('ok finally!')
```

### 예외처리5 - 예외를 계층적으로 처리
```
name = ['lee', 'kim', 'park']
try:
    z = 'kim'
    x = name.index(z)
    print('{} found it! in name'.format(z))
except ValueError as ve:
    print(ve)
except IndexError as ie:
    print(ie)
except Exception:
    print('Exception')
else:
    print('else')
finally:
    print('finally')
```

### 예외6 - 예외를 직접 발생
```
try:
    a = 'lee'
    if a == 'lee':
        print('ok')
    else:
        raise ValueError 
except ValueError:
    print('value error')
except Exception as f:
    print(f)
else:
    print('ok')
```

<br>[Contents](#Contents)<br><br>

## 파이썬 외부파일 처리
- csv : mime - text/csv

## 1. CSV

#### ex1
```
import csv
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    # next(reader) - csv table Header 스킵하기
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    for c in reader:
        print(c)
```

#### ex2 - 구분자 사용 delimiter
```
with open('./resource/sample2.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader) - csv table Header 스킵하기
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    for c in reader:
        print(c)
```

#### 예제3 - Dict 변환
```
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.DictReader(f)

    for c in reader:
        print(c)
        for k, v in c.items():
            print(k,v)
        print('-----------')
```

#### ex4 - csv 쓰기
```
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)
```

## 2. Excel 읽기/쓰기
- 엑셀(XSL, XLSX)
- XSL은 이전 버전
- 엑셀처리 라이브러리 : openpyxl, xlsxwriter, xlrd, xlwt, xlutils, ...
- pandas를 사용한다(pandas는 openpyxl, xlrd를 사용)
- pandas는 데이터조작과 분석을 위한 파이썬 라이브러리
- pip install xlrd
- pip install openpyxl
- pip install pandas

#### 기본문법
```
import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx', engine='openpyxl')

print(xlsx.head())
print(xlsx.tail())
print(xlsx.shape) # 행, 열의 수
```

#### 엑셀 or CSV 다시쓰기
```
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
```

<br>[Contents](#Contents)<br><br>

