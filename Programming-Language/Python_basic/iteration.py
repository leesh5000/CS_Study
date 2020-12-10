# Section05-2
# 반복문
# for, while

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

# 시퀀스 자료형 + 문자열, 리스트, 튜플, 집합, 사전은 반복가능
# iterable 리턴함수 : range, reversed, enumerate, filter, map, zip, ...

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

# for-else
numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if (i==17):
        print("Found : %d" % i)
        break
else:
    print("Not found 7")


name = "helloC"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))