# Section 05-1
# 조건문 실습

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

# True, False 종류
# 1. True : "내용", [내용], (내용), {내용}, 1
# 2. False : "", [], (), {}, 0

str_test = ""

if str_test:
    print("T")
else:
    print("F")

# 논리연산자 : and, or, not

a = 100
b = 60
c = 15

print('and :', a>b and b>c)
print('or :', a>b or c>b)
print('not :', not a>b)

# 산술(+,-,..), 관계(>,=,<,..), 논리(and,or,not) 연산자 우선순위
# 산술 > 관계 > 논리

print('test : ', 5+10>0 and not 7+3==10)

# 다중조건문
num = 100

if num>=90:
    print("A", num)
elif num >=80:
    print("B", num)
elif num >=70:
    print("C", num)
else:
    print("F", num)

# 중첩조건문
