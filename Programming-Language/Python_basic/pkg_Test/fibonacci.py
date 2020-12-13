class Fibo:
    def __init__(self, title="fibo"):
        self.title = title
    
    @staticmethod
    def fib1(n):
        a, b = 0, 1
        while a<n:
            print(a, end=' ')
            a,b=b,a+b
        print()
    
    @staticmethod
    def fib2(n):
        result = []
        a, b = 0, 1
        while a<n:
            result.append(a)
            a,b=b,a+b
        return result