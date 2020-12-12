# 스택사용 - 파이썬

s = []
s.append(1)
s.append(2)

while len(s) != 0:
    print(s.pop())

# 스택구현
s1 = []

def push(data):
    s1.append(data)

def pop():
    return s1.pop()

push(10)
push(100)
push(999)
print(pop())
