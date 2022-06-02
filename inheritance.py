class A:
    def __init__(self,a):
        self.a = a
        self.fun()

    def fun(self):
        print(self.a)

    def my_func(self):
        print(self.a ** 2)


class B(A):
    def __init__(self,a):
        super().__init__(a)
        self.b = 20

    def b_func(self):
        print(self.a)


b = B(5)
b.my_func()