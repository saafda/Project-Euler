import math
def func(n):
    m = n - 1
    r = m * 2
    pascalnumber = (math.factorial(r)) / (math.factorial(r - m) * math.factorial(m))
    return pascalnumber
print(func(21))
