def quadratic(a, b, c):
    return lambda x : a * x ** 2 + b * x + c

f = quadratic(1,2,3)
print(f)
print(f(1))
