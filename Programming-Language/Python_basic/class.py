# section07-1
# 파이썬 클래스
# self, 인스턴스 변수, 클래스

# 선언
# __init__은 c언어의 생성자 같은 것
# self는 클래스의 인스턴스 변수
# 클래스 : 붕어빵 틀
# 객체 : 소프트웨어에서 구현할 실제대상
# 인스턴스 : 붕어빵, 객체를 메모리에 할당한 것
class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Class Initiated!")
    def Print_Info(self):
        print("Name : %s\nAge : %d\n" % (self.name, self.age))

user1 = UserInfo("LSH", 27)
user1.Print_Info()

user2 = UserInfo("KYJ", 24)
user2.Print_Info()

# 클래스의 네임스페이스
print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 2. 클래스매소드와 인스턴스매소드
# - 클래스변수 : 클래스에서 직접사용 가능
# - 인스턴스변수 : 인스턴스마다 별도로 존재, 인스턴스 생성 후 사용
class SelfTest:
    # 클래스 매소드
    def func1():
        print('func1 called!')
    # 인스턴스 매소드
    def func2(self):
        print('func2 called!')
        print(id(self))

self_Test1 = SelfTest()
self_Test1.func2()
SelfTest.func1()

print(id(self_Test1))
SelfTest.func2(self_Test1)

# 3. 클래스변수 인스턴스변수(self)
# - 클래스변수 : 모든 인스턴스 변수가 공유, 네임스페이스는 클래스명
# - 인스턴스변수 : 인스턴스마다 별도로 존재, 네임스페이스는 인스턴스명
class Warehouse:
    # 클래스 변수, 각각 인스턴스 변수가 공유, static변수와 같은것?
    num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.num += 1
    def __del__(self):
        Warehouse.num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Kim')
user3 = Warehouse('Park')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(Warehouse.__dict__)

print(user1.num)
print(user2.num)
print(user3.num)

del user1

print(user2.num)
print(user3.num)

