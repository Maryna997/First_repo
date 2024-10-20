def f1():
    a = 7
    def f2():
        nonlocal a
        a = 3
    f2()
    print(a)

f1()


