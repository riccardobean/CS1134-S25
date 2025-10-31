def section_a(n):
    add = 0
    for i in range(n):
       add += i*i
    return add

def section_b(n):
    return sum([x*x for x in range(n)])

def section_c(n):
    add = 0
    for i in range(1, n, 2):
       add += i*i
    return add

def section_d(n):
    return sum([x*x for x in range(n) if x % 2 != 0])
