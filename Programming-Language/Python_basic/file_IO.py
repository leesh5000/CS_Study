# section09
# 파일 I/O
# 읽기모드 : r
# 쓰기모드(덮어쓰기) : w
# 추가모드 : a

# 파일읽기1
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
f.close()

# 파일읽기2
# with는 close를 안해도 자동으로 close 해준다.
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    
# 파일읽기3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

# 파일읽기4 
# - 한번 read를 하면 커서가 파일 끝으로 가서 더 읽을게 없음
with open('./resource/review.txt', 'r') as f:
    contents1 = f.read()
    contents2 = f.read()
    print("c1>>", contents1)
    print("c2>>", contents2)

# 파일읽기5
# - 한줄씩 읽어오기
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    print(line)
    while line:
        print(line, end=' #### ')
        line = f.readline()

# 파일읽기6
# - readlines는 list를 반환
with open('./resource/review.txt', 'r') as f:
    c1 = f.readlines()
    print(c1)
    for c in c1:
        print(c, end= ' #### ')


print('\n\n')

# 예제
# - score파일 읽어서 평균내기
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Average : {:6.3}".format(sum(score)/len(score)))

# 파일쓰기1
with open('./resource/text1.txt', 'w') as f:
    f.write("Nice man!\n")

with open('./resource/text1.txt', 'a') as f:
    f.write("Good man!\n")

# 파일쓰기2
from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 파일쓰기3 
# - 리스트형태를 파일로 쓰기
with open('./resource/text3.txt', 'w') as f:
    list = ['lee\n', 'kim\n', 'park\n']
    f.writelines(list)

# 파일쓰기4
# - print문으로 파일쓰기
with open('./resource/text2.txt', 'w') as f:
    print('Test1', file=f)
    print('Test2', file=f)

    