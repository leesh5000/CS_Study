# 딕셔너리와 셋

# 딕셔너리(dicionary) : 순서x, 중복x(key만), 수정o, 삭제o
# key, value (Json)
# 딕셔너리는 웹 브라우저 데이터 송신에 사용되는 Json 형식과 비슷

# 선언
a = {'name': 'Lee', 'phone': '010-0000-0000', 'address': '12345'}
b = {0: 'Hello Python', 1: 'Hello Java'}
c = {'arr': [1,2,3,4,5], 'tuple': (1,2,3,4,5,)}

print(type(a))
print(a['name'])
print(a.get('name'))
print(a.get('birth'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['birth'] = '941008'
print(a)
a['rank'] = [1,2,3]
a['rank2'] = (1,2,3,)
print(a)

# keys, values, items
print(a.keys())
# print(a.keys()[2]) # 에러
print(list(a.keys())[1:3])
print(a.values())
print(a.items())
temp = list(a.items())
print(temp)
print(2 in b)
print('name' in a)




