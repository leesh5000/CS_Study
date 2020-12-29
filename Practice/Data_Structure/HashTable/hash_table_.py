# Hash Table
# - key와 value를 저장하는 자료구조
# - 키 값으로 데이터에 접근하므로 데이터의 조회가 O(1)의 시간복잡도를 갖는다.
# - 충돌을 해결하기 위한 별도의 저장공간이 필요
# - 데이터의 조회,저장,삭제가 빈번한 경우 사용

# 충돌을 해결하는 방법
# Open Addressing Method : 충돌 발생 시, 다른 자리에 대신 저장하는 방법
# 1. Linear Probing
# 2. Quadratic Probing
# 3. Double Hashing
# Close Addressing Method : 충돌 발생 시, 원래 해쉬주소에 저장
# 1. Chaining

class hash_table:
    def __init__(self, len):
        self.lt = [None for i in range(len)]
    # 해쉬 키 값을 추출하는 함수
    def hash_key(self, key):
        return ord(key[0])
    # 해쉬 주소값을 추출하는 함수
    def hash_func(self, hash_key):
        return hash_key % len(self.lt)
    # 선형조사법 사용
    def insert(self, key, value):
        hash_key = self.hash_key(key)
        hash_addr = self.hash_func(hash_key)
        # 만약, key값의 해쉬주소에 이미 데이터가 있다면,
        if self.lt[hash_addr] != None:
            # 현재 해쉬주소 + 1 을 하면서
            for i in range(hash_addr+1, len(self.lt)):
                # 빈공간이 있으면 넣기
                if self.lt[i] == None:
                    self.lt[i] = [key, value]
                    return
                # 만약, 똑같은 키 값을 가진 데이터가 테이블 안에 있다면, 덮어쓰기
                elif self.lt[i][0] == key:
                    self.lt[i][1] = value
                    return
        # 만약, key값의 해쉬주소에 데이터가 없다면,
        else:
            self.lt[hash_addr] = [key, value]

    # 데이터 조회
    def search(self, key):
        hash_key = self.hash_key(key)
        hash_addr = self.hash_func(hash_key)
        # 해당 해쉬주소에 데이터가 있다면,
        if self.lt[hash_addr] != None:
            # 현재 해쉬주소 부터 끝까지 돌면서
            for i in range(hash_addr, len(self.lt)):
                # 만약, 키 값이 같으면, value를 반환해주기
                if self.lt[i][0] == key:
                    return self.lt[i][1]

ht = hash_table(10)
ht.insert('LSH','010-0000-0000')
ht.insert('KYJ','010-1111-1111')
ht.insert('LCH','010-2222-2222')
ht.insert('MHS','010-3333-3333')
ht.insert('LSHH','010-4444-4444')
print("LSH : {}, KYJ : {}, LCH : {}, MHS : {}, LSHH : {}".format(ht.search('LSH'),
ht.search('KYJ'), ht.search('LCH'), ht.search('MHS'), ht.search('LSHH')))
