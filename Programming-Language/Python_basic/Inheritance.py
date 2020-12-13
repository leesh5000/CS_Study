# section07-2
# 파이썬 클래스 상속 
# 클래스 상속
# 파이썬은 다중상속 지원
# 자바는 인터페이스 지원, 다중상속 지원x

# 상속
# - 코드의 재사용, 생산성 향상
# - 부모클래스의 모든 속성,메소드 사용 가능
# - 부모클래스 = 상위클래스 = 슈퍼클래스
# - 자식클래스 = 하위클래스 = 서브클래스

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def Show_Info(self) -> None:
        return 'Car Class "Show Method!"'

class BMW(Car):
    """Child Class"""
    def __init__(self, name, tp, color):
        super().__init__(tp, color)
        self.name = name
    
    def Show_Name(self) -> None:
        return "Your Car Name : %s" % self.name

car1 = BMW('520d', 'sedan', 'red')
print(car1.color)
print(car1.type)
print(car1.name)
print(car1.Show_Info())
print(car1.Show_Name())

print(car1.__dict__)

# 오버라이딩
class Benz(Car):
    """Child Class"""
    def __init__(self, name, tp, color):
        super().__init__(tp, color)
        self.name = name
    
    def Show_Name(self) -> None:
        return "Your Car Name : %s" % self.name

    def Show_Info(self) -> None:
        print(super().Show_Info())
        return "Benz Overriding"

car2 = Benz('220d', 'suv', 'white')
print(car2.Show_Info())

# Inheritance Info
# - 상속 정보를 리스트 형태로 반환해주는 매소드
# - 왼쪽에서 오른쪽으로 상위 클래스 이름이 나옴
print(BMW.mro())
print(Benz.mro())

# 다중상속
class X():
    pass

class Y():
    pass

class A(X,Y):
    pass

print(A.mro())
