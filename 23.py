def f(a):
    if a >= 100: return tuple()
    if a % 2 == 1: return tuple([a]) + f(a + 3) + f(a * 3)
    return f(a + 3) + f(a * 3)

print(len(set(f(10))))
