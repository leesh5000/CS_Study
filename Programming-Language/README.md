## Programmin Language

## Contents

- [Python](#python)
  - [파이썬의 장점](#파이썬의-장점)
  - [기본출력](#기본출력)
  - [파이썬의 데이터타입](#파이썬의-데이터타입)
    - [기본자료형](#기본자료형)
    - [문자열](#문자열)
    - [리스트와 튜플](#리스트와-튜플)
    - [딕셔너리](#딕셔너리)
    - [집합](#집합)
  - [코드의 흐름제어](#코드의-흐름제어)
    - [조건문](#조건문)
    - [반복문](#반복문)
  - [함수](#함수)
    - [*args, *kwargs](#args-kwargs)
    - [중첩함수(클로저)](#중첩함수클로저)


<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

# Python

## 파이썬의 장점
- 사용하기 쉽다.
- 파이썬 인터프리터만 있으면 어느 운영체제든지 실행가능하다.
- 다양한 라이브러리가 존재한다.
- 과학, 머신러닝, 웹 등 범용적으로 사용된다.

<br>[Contents](#Contents)<br><br>

## 기본출력

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

<br>[Contents](#Contents)<br><br>

## 기본자료형
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

## 문자열
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

## 리스트와 튜플
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

<br>[Contents](#Contents)<br><br>

## 튜플
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

## 딕셔너리
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

## 집합
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

## 조건문
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

### True, False 종류
- True : "내용", [내용], (내용), {내용}, 1
- False : "", [], (), {}, 0
```
str_test = ""

if str_test:
    print("T")
else:
    print("F")
```

### 논리연산자 : and, or, not
```
a = 100
b = 60
c = 15

print('and :', a>b and b>c)
print('or :', a>b or c>b)
print('not :', not a>b)
```

### 연산자 우선순위
- 산술(+,-,..), 관계(>,=,<,..), 논리(and,or,not) 연산자 우선순위
- 산술 > 관계 > 논리
```
print('test : ', 5+10>0 and not 7+3==10)
```

### 다중조건문
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

## 반복문

### for, while
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

### 시퀀스 자료형, 문자열, 리스트, 튜플, 집합, 사전은 반복가능
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

### for-else
```
numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if (i==17):
        print("Found : %d" % i)
        break
else:
    print("Not found 7")
```

### 자료구조 변환
```
name = "helloC"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
```

<br>[Contents](#Contents)<br><br>

## 함수
- 하나의 함수에 하나의 기능만

### 기본문법
```
def Hello(word):
    print("Hello", word)

Hello("python")

def sum_int(a, b):
    return a+b

print(sum_int(4,6))
```

### 다중리턴
```
def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1,y2,y3

val1, val2, val3 = func_mul(5)
print(val1, val2, val3)
```

### 데이터타입 반환
```
def func_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1,y2,y3]

lt = func_mul2(5)
print(lt)
```

## *args, *kwargs

### *args : 가변인자
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

### *kwargs
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

### 중첩함수(클로저)
```
def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)
```

<br>[Contents](#Contents)<br><br>
