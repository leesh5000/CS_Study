# ord() : 문자의 ASCII코드 리턴하는 함수
# 아스키코드는 유니코드 이전에 쓰던 방식
# 아스키코드의 단점은 영어와 특수문자 정도 밖에 못한다.

class HashTable:
    @staticmethod
    def hash_func(str_key):
        return ord(str_key[0])%5
    
    def __init__(self):
        self.lt = [i for i in range(10)]
    
    def add(self, key, value):
        hash_addr = self.hash_func(key)
        self.lt[hash_addr] = value

    def get(self, key):
        return self.lt[self.hash_func(key)]

ht = HashTable()
ht.add('lsh', '010-1111-2222')
ht.add('kyj', '010-3333-2222')
print(ht.get('lsh'))