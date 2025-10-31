import math

def factors(num):
    yield 1
    factor = []
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            factor.append(i)
            yield i
    if num % math.sqrt(num) == 0:
        yield int(math.sqrt(num))

    for el in factor[::-1]:
        yield num // el
    yield num
