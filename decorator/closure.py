def outer(k,b):
    def inner(x):
        return k * x + b
    return inner

f = outer(2,3)
print(id(f))
print(f(2))
f = outer(1,5)
print(id(f))
print(f(2))


def f1():
    x = 10
    def f2():
        nonlocal x
        x = 15
        print(x)
    return f2

f = f1()
f()