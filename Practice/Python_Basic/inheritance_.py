# 부모클래스
class parent():
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(self.name)

# 자식클래스
class child(parent):
    pass

p = parent('parent')
c = child('child')

p.show_info()
c.show_info()