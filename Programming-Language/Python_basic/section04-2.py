# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = "NiceMan"
str3 = ' '

print(len(str1), len(str2), len(str3))  # 9,7,1 출력

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)  # Do you have a big collection
escape_str2 = "Tab\tTab"
print(escape_str2)  # Tab     Tab

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)  # C:\Programs\Test\Bin
raw_s2 = r"\n\t''"
print(raw_s2)  # \n\t''

# 멀티라인
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

# 문자열 연산
str_o1 = "*"
str_o2 = 'abc'
str_o3 = 'def'

print(str_o1 * 30)  # ******************************
print(str_o3 + str_o2)  # defabc

str_o4 = "Niceman"  # ""는 immutable로 한번 할당되면 수정이 불가능한 시퀀스. 순회가 가능하다.
print('a' in str_o4)  # immutable은 순회가 가능
print('z' not in str_o4)  # True

# 문자열 형변환
print(str(77) + 'a')  # 77a

# 문자열 관련 함수
a = "niceman"
b = "orange"

print(a.islower())  # True
print(b.endswith('e'))  # True
print(a.capitalize())  # Niceman
print(a.replace('nice', 'good'))  # goodman
print(list(reversed(b)))  # ['e', 'g', 'n', 'a', 'r', 'o']

# 문자열 슬라이싱
# 파이썬에서 immutable은 변경불가능한 자료형을 말한다.
# 문자열이 각각의 인덱스를 갖고 있기 때문에 파이썬에서 문자열은 immutable이다.

c = 'niceman'
d = 'orange'

print(c[0:3])  # nic
print(c[0:len(c)])  # niceman
print(c[:4])  # nice
print(c[:])  # niceman
print(d[0:4:2])  # oa
print(d[1:-2])  # ran
print(d[::-1])  # egnaro

a = 1
b = 2
c = 3
d = 4
e = 5
print(a, b, c, d, e, sep=' t ')
