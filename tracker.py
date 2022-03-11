def func_counter(func):
    counter = 0

    def inner(*x):
        func(*x)
        inner.counter += 1

    inner.counter = 0
    return inner


@func_counter
def foo(y):
    return y + 2 ** 3 - 34

y = 1
for _ in range(100):
    foo(y)
print(foo.counter)
