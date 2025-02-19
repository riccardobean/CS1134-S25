def e_approx(n):
    fact = 1
    e = 1
    for i in range(1, n + 1):
        fact *= i
        e += 1 / fact
    return e