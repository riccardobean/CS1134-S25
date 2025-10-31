def fibs(n):
    num1 = 0
    num2 = 1
    next = 1
    yield next
    yield next
    for i in range(n - 2):
        num1 = num2
        num2 = next
        next = num1 + num2
        yield next
