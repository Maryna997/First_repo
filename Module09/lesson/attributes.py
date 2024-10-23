class A:
    b = 5

    def __init__(self, x):
        self.x = x

a = A(x=3)
print(a.x)
print(a.b)
print(A.b)