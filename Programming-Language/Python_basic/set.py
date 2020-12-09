# 집합

# 집합(sets) : 순서x, 중복x
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 6, 6, 6])

print(type(a))
print(c)

# 셋은 주로 변환을 해서 사용한다.
t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1 - s2)
print(s1.difference(s2))

# 추가/제거
s3 = set([7, 8, 9, 15])
s3.add(18)
s3.add(7)
print(s3)
s3.remove(15)
print(s3)