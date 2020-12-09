# Section05
# 파이썬 데이터 타입
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)

# 리스트 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c+d)
print(c*3)
print(str(c[0])+'hi')

# 리스트 수정/삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000] # 슬라이싱 처리를 하고 리스트를 넣으면
print(c)
c[1] = [100, 1000, 10000] # 슬라이싱 처리를 하지 않고 리스트를 넣으면
print(c)

del c[1]
print(c)

del c[-1]
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
y.remove(2) # remove는 값에 해당하는 원소를 삭제
print(y)
y.pop()
print(y)
ex = [88, 77]
y.extend(ex)
y.append(ex)
print(y)

# 튜플
# 튜플(순서o, 중복o, 수정x, 삭제x)
# 변경되면 안되는 중요한 값이 저장되는 곳에 쓰임

# 튜플의 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# 튜플 인덱싱
print(c[2])
print(d[2][1])

# 튜플 슬라이싱
print(d[2:])
print(d[2][0:2])

# 연산
print(c+d)
print(c*3)

# 튜플함수
e = (5,2,1,3,4,1)
print(e)
print(3 in e)
print(e.index(5))
print(e.count(1))