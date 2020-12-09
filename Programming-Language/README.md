## Programmin Language

## Contents

- [Python](#python)
  - [파이썬의 장점](#파이썬의-장점)
  - [기본출력](#기본출력)
  - [파이썬의 데이터타입](#파이썬의-데이터타입)
    - [기본자료형](#기본자료형)
    - [문자열](#문자열)
    - [리스트와 튜플](#리스트와-튜플)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

## Python

### 파이썬의 장점
- 사용하기 쉽다.
- 파이썬 인터프리터만 있으면 어느 운영체제든지 실행가능하다.
- 다양한 라이브러리가 존재한다.
- 과학, 머신러닝, 웹 등 범용적으로 사용된다.

<br>[Contents](#Contents)<br><br>

### 기본출력

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

### 파이썬의 데이터타입
- Boolean
- Numbers
- String
- Bytes
- Lists
- Tuples
- Sets
- Dictionaries

### 기본자료형
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

### 문자열
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

### 리스트 선언
```
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]
```

### 리스트 인덱싱
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

### 슬라이싱
```
print(d[0:3])
-> [10, 100, 'Pen']

print(e[2][1:3])
-> ['Banana', 'Orange']
```

### 연산
```
print(c+d)
-> [1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']

print(c*3)
-> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

print(str(c[0])+'hi')
-> 1hi
```

### 리스트 수정/삭제
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

### 리스트 함수
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

## 튜플
- 튜플(순서o, 중복o, 수정x, 삭제x)
- 변경되면 안되는 중요한 값이 저장되는 곳에 쓰임

### 튜플의 선언
```
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
e = tuple()
```

### 튜플 인덱싱
```
print(c[2])
-> 3

print(d[2][1])
-> b
```

### 튜플 슬라이싱
```
print(d[2:])
-> (('a', 'b', 'c'),)

print(d[2][0:2])
-> ('a', 'b')
```

### 연산
```
print(c+d)
-> (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))

print(c*3)
-> (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

```

# 튜플함수
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