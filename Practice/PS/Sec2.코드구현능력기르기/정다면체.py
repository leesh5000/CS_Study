# 정다면체
# - 파이썬 dict.get(key)은 해당하는 key값의 값이 있으면 해당 value를 없으면 None을 리턴
# - key in dict는 값이아니라 True, False로 리턴
# - list comprehension을 {}로 하면 set comprehension
# - list comprehension을 {}로 하고 동시에 key, value를 넣어주면 dictionary comprehension

for i in range(1,6):
    f1 = open('./PS/source/in{}.txt'.format(i), 'r')
    n, m = map(int, f1.readline().split())

    # 나올 수 있는 값을 Key로 하는 딕셔너리로 초기화
    d = {i : 0 for i in range(2, n+m+1)}

    # 두 수를 던져서 나오는 모든 경우의 수에 대해 dict 값 넣어주기
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i+j in d:
                d[i+j] += 1

    # 제일 많이 나오는 두 눈의 합을 출력하기]
    ans = [k for k,v in d.items() if v == max(d.values())]
    print(' '.join(map(str, ans)))
    
    # for k, v in d.items():
    #     if v == max(d.values()):
    #         print(k, end=' ')
    
    # print('\n')

