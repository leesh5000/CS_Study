# 파이썬 데이터타입
import math  # 수학관련 모듈
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}

v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7]

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999991293810
big_int2 = 1092810724129040124801294817
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

# 연산
print(i1*i2)
print(big_int1 * big_int2)
print(f1 ** f2)

result = f3 + i2
print(result, type(result))

# 형 변환
a = 5.
b = 10

print(type(a), type(b))
result2 = a+b

print(result2, type(result2))  # 15.0을 출력
print(int(result2))
print(int('3'))

# 수치 연산 함수
print(abs(-7))
n, m = divmod(100, 8)  # n = quotient , m = remainder

print(math.ceil(5.1))  # 5.1보다 크면서 가장 작은 정수 = 6
print(math.floor(3.874))  # 3.874보다 작으면서 가장 큰 정수 = 3


4
