# # ord() : 문자의 ASCII코드 리턴하는 함수
# # 아스키코드는 유니코드 이전에 쓰던 방식
# # 아스키코드의 단점은 영어와 특수문자 정도 밖에 못한다.

# # 1. 해쉬키 생성
# # 2. 해쉬함수(해쉬키) = 해쉬주소
# class HashTable:
#     @staticmethod
#     def hash_func(str_key):
#         return ord(str_key[0])%5
    
#     def __init__(self):
#         self.lt = [i for i in range(10)]
    
#     def add(self, key, value):
#         hash_addr = self.hash_func(key)
#         self.lt[hash_addr] = value

#     def get(self, key):
#         return self.lt[self.hash_func(key)]

# ht = HashTable()
# ht.add('lsh', '010-1111-2222')
# ht.add('kyj', '010-3333-2222')
# print(ht.get('lsh'))

# ## 해쉬테이블 연습
# ht = [0 for i in range(8)]

# def get_key(data):
#     return hash(data)

# def ht_func(key):
#     return key % 8

# def save_data(data, value):
#     idx_key = get_key(data)
#     ht_addr = ht_func(idx_key)

#     if ht[ht_addr] != 0:
#         for idx in range(len(ht[ht_addr])):
#             if ht[ht_addr][idx][0] == idx_key:
#                 ht[ht_addr][idx][1] = value
#                 return
#         ht[ht_addr].append([idx_key, value])
#     else:
#         ht[ht_addr] = [[idx_key, value]]

# def read_data(data):
#     idx_key = get_key(data)
#     ht_addr = ht_func(idx_key)

#     if ht[ht_addr] != 0:
#         for idx in range(len(ht[ht_addr])):
#             if ht[ht_addr][idx][0] == idx_key:
#                 return ht[ht_addr][idx][1]
#         return None
#     else:
#         return None

# save_data('Dd', '27')
# save_data('Data', '24')
# print(read_data('Dd'))
# print(ht)

ht = [0 for i in range(8)]

def get_key(data):
    return hash(data)

def ht_func(key):
    return key % 8

def save_data(data, value):
    idx_key = get_key(data)
    ht_addr = ht_func(idx_key)

    if ht[ht_addr] != 0:
        for idx in range(ht_addr, len(ht)):
            if ht[idx] == 0:
                ht[idx] = [idx_key, value]
                return
            # 키가 동일하면 값을 업데이트
            elif ht[idx][0] == idx_key:
                ht[idx][1] = value
                return
    else:
        ht[ht_addr] = [idx_key, value]

def read_data(data):
    idx_key = get_key(data)
    ht_addr = ht_func(idx_key)

    if ht[ht_addr] != 0:
        for idx in range(ht_addr, len(ht)):
            if ht[idx] == 0:
                return None
            elif ht[idx][0] == idx_key:
                return ht[ht_addr][idx][1]
    else:
        return None

# SHA-1 사용
import hashlib
data = 'test'.encode()
hs_obj = hashlib.sha256()
# 스트링 'test'를 byte로 바꿔주기
# byte로 해야 sha1을 사용가능
# 'test'.encode로도 가능
hs_obj.update(data)
# 해쉬화된 값을 16진수로 추출하기 (주로 16진수로 추출함)
hex_dig = hs_obj.hexdigest()
print(hex_dig)