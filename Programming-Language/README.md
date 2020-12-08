## Programmin Language

## Contents
- [Python](#python)
  - [파이썬의 장점](#파이썬의-장점)
  - [기본출력](#기본출력)
  - [파이썬의 데이터타입](#파이썬의-데이터타입)
  - [연산](#연산)
  - [문자열](#문자열)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

## Python

### 파이썬의 장점
- 사용하기 쉽다.
- 파이썬 인터프리터만 있으면 어느 운영체제든지 실행가능하다.
- 과학, 머신러닝, 웹 등 범용적으로 사용된다.

<br>[Contents](#Contents)<br><br>

### 기본출력
기본출력
```
print('Hello Python!')

print("Hello Python!")

print("""Hello Python!""")

print('''Hello Python!''')
```

줄바꿈
```
print()

```

Seperate 옵션 사용
```
print('T', 'E', 'S', 'T', sep='')

print('2020','09','07', sep='-')

print('leesh5000','google.com', sep='@')
```

End 옵션 사용
```
print('Hi', end=' Python')

print('\nPython is ', end='Good\n')

```

format 옵션 사용
```
print("\n[format 옵션 사용]")

print('{} and {}'.format(1,2))

print("{0} and {1} and {0}".format('zero','one'))

print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('SH', 7))

print("Test1 : %5d, Price : %4.2f" % (101, 1234.56789))

print("Test2 : {0: 5d}, Price : {1: 4.2f}".format(101,1234.567))

print("Test3 : {a: 5d}, Price : {b: 4.2f}".format(a=101,b=1234.567))

```

Escape 코드
```
print("\n[Escape 코드 사용]")

print("'you'")

print('"Hi"')

print('\'Hello\'')

print('\\Python\\')

print('\\n\n')

print('\ttap')

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

print(type(v_set))

print(type(v_float))
```

#### 형 변환
```
a = 5.
b = 10

print(type(a), type(b))

result2 = a+b

print(result2, type(result2)) 
## 15.0을 출력

print(int(result2))

print(int('3'))
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

#### 형 변환
```
a = 5.
b = 10

print(type(a), type(b))
result2 = a+b

print(result2, type(result2))
## 15.0을 출력

print(int(result2))

print(int('3'))
```

#### 수치 연산 관련 함수
```
print(abs(-7))
n, m = divmod(100, 8) 
## n = quotient , m = remainder

import math ## 수학관련 모듈 

print(math.ceil(5.1)) 
## 5.1보다 크면서 가장 작은 정수 = 6

print(math.floor(3.874))
## 3.874보다 작으면서 가장 큰 정수 = 3
```

<br>[Contents](#Contents)<br><br>

### 문자열
```
str1 = "I am Boy."
str2 = "NiceMan"
str3 = ' '

print(len(str1), len(str2), len(str3))
## 9,7,1 출력

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
## Do you have a big collection

escape_str2 = "Tab\tTab"
print(escape_str2)
## Tab     Tab
```

#### Raw String
```
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
## C:\Programs\Test\Bin

raw_s2 = r"\n\t''"
print(raw_s2)
## \n\t''
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
# ******************************

print(str_o3 + str_o2)
# defabc

str_o4 = "Niceman" # ""는 immutable로 한번 할당되면 수정이 불가능한 시퀀스. 순회가 가능하다.
print('a' in str_o4)
# immutable은 순회가 가능

print('z' not in str_o4)
# True
```

#### 문자열 형변환
```
print(str(77) + 'a') # 77a
```

#### 문자열 관련 함수
```
a = "niceman"
b = "orange"

print(a.islower())
# True

print(b.endswith('e'))
# True

print(a.capitalize())
# Niceman

print(a.replace('nice','good'))
# goodman

print(list(reversed(b)))
# ['e', 'g', 'n', 'a', 'r', 'o']
```

#### 문자열 슬라이싱
- 파이썬에서 immutable은 변경불가능한 자료형을 말한다.
- 문자열이 각각의 인덱스를 갖고 있기 때문에 파이썬에서 문자열은 immutable이다.

```
c = 'niceman'
d = 'orange'

print(c[0:3])
# nic

print(c[0:len(c)])
# niceman

print(c[:4])
# nice

print(c[:])
# niceman

print(d[0:4:2])
# oa

print(d[1:-2])
# ran

print(d[::-1])
# egnaro
```

<br>[Contents](#Contents)<br><br>
