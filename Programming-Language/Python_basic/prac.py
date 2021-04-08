# # c = [1, 2, 3]

# # # 인덱싱으로 넣으면 원소가 들어감
# # c[1:2] = [10, 100, 1000]
# # print(c)
# # # 인덱스로 넣으면 리스트가 들어감
# # c[2] = [10, 100, 1000]
# # print(c)

# # # append는 리스트 / extend는 원소
# # a = [1, 2, 3, 4]
# # b = [5, 6, 7]
# # a.append(b)
# # a.extend(b)
# # print(a)

# # # 삭제 : del(인덱스), remove(값)

# # # 튜플 : 순서,중복o / 수정,삭제x
# # # (변경되면 안되는) 중요한 값을 저장되는데에 쓰임

# # # 튜플 안의 리스트는 변경될 수 있음
# # a = ()
# # b = (1, [2, 3, 4])
# # b[1][2] = 10
# # print(b)

# # # 튜플은 del 불가
# # a = (1, 2, 3, 4)
# # # del a[2]

# # # 튜플함수
# # a = (1, 5, 2, 1, 3, 4, 2, 1)
# # print(3 in a)
# # print(a.index(1))
# # print(a.count(1))

# # # 딕셔너리 : 순서x 중복x 수정o 삭제o
# # # 1. 키는 중복 불가, 값은 중복 가능
# # # 2. 파이썬의 딕셔너리 안에는 어떠한 데이터 타입이든지 넣을 수 있다.
# # # 3. get() 메소드의 활용
# # print()
# # a = {'name': 'lee'}
# # print(a['name'])
# # print(a.get('age'))

# # # 4. 딕셔너리 추가
# # a['age'] = '19'

# # # 5. keys, values, items
# # # // 형변환해서 인덱스 접근해야함
# # # // items()는 list안에 tuple로 반환
# # a = {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4}
# # print(a.keys())
# # print(list(a.keys()))
# # print(a.values())
# # print(a.items())
# # print('ee' in a)

# # # 집합 : 순서x, 중복x,
# # a = set()
# # # 집합은 리스트로 넣어야함
# # b = set([1, 2, 3, 4, 5, 5])
# # print(b)
# # s1 = set([1, 2, 3, 4, 5, 6])
# # s2 = set([4, 5, 6, 7, 8, 9])

# # # Set - 교집합 함수
# # print(s1.intersection(s2))
# # print(s1 & s2)
# # print(s1.union(s2))
# # print(s1 | s2)

# # # 차집합
# # print(s1-s2)
# # print(s1.difference(s2))

# # # 추가 & 제거
# # s1 = set([7, 8, 9, 15])
# # s1.add(18)
# # s1.remove(8)
# # print(s1)

# # # 참 거짓 종류
# # # 참 : 내용이 있는 문자열, 내용이 있는 리스트/튜플/딕셔너리, 1
# # # 거짓 : 빈 문자열, 빈 리스트/튜플/딕셔너리, 0

# # # 논리연산자
# # # and or not

# # # 산술, 관계, 논리연산자
# # # 산술(+,-,..) > 관계(and, or) > 논리(not)

# # # sum 함수
# # print(sum(range(1, 100)))

# # # 시퀀스(순서가 있는 자료형)는 for문에서 반복 가능
# # # 시퀀스자료형(iterable) 외에 문자열, 리스트, 튜플, 집합, 사전도 반복 가능
# # # range, reversed, enumurate, filter, map, zip는 iterable 리턴 함수

# # d = {
# #     'aa': 1,
# #     'bb': 2,
# #     'cc': 3,
# # }

# # for x in d.items():
# #     print(x)

# # # 파이썬 for - else
# # # - 반복문이 정상적으로 수행된 경우 else 블럭 수행
# # # break가 실행되면 else문 실행x
# # # break가 없으면 for문 다 수행되고 마지막에 else 실행
# # numbers = [1, 2, 3, 4, 5, 6, 7]
# # for num in numbers:
# #     if num == 10:
# #         print("num")
# #         break
# #     else:
# #         print("not found")
# # else:
# #     print("not found")

# # # 리스트 컴프리헨션
# # n = [x for x in range(1, 101)]
# # print(n)

# # ''' ----------- 2/24 Wed. Test #3 ----------------- '''
# # 함수식 및 람다

# # 1. 파이썬 함수는 다중리턴 지원)

# # import copy
# # a = [[1, 2, 3], (4, 5, 6)]
# # b = list(a)
# # c = copy.deepcopy(a)
# # print(id(a), id(a[0]), id(a[1]))
# # print(id(b), id(b[0]), id(b[1]))
# # print(id(c), id(c[0]), id(c[1]))

# # a = [1, 2, 3, 4]
# # b = [1, 2, 3, 4]
# # print(id(a), id(b))

# # c = (1, 2, 3, 4)
# # d = (1, 2, 3, 4)
# # print(id(c), id(d))

# # e = 'test'
# # f = 'test'
# # print(id(e), id(f))

# def func(x, y):
#     x.append(list(y))
#     y.append(2)
#     return x


# x = [1, 2]
# y = [3, 4]
# z = func(x, y)
# print(x, y, z)

import array
init = [1, 2, 3, 4, 5, -6]
a = array.array('i', init)
b = array.array('i', [0]*len(a)*2)
b[:len(a)] = a
b[len(a):] = array.array('i', [6, 7, 8, 9, 10])
print(b)
print(a)
