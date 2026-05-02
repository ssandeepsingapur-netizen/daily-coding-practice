class A:
    def __init__(self):
        self.value = 200

class B:
    def __init__(self):
        self.obj = A()   # object of A

    def show(self):
        print(self.obj.value)

b = B()
b.show()