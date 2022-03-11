def doubler(func):
    def inner():
        func()
        func()
    return inner