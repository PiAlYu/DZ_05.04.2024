def f(a):
    for x in range(1, 300):
        f = (x // 50 > 3) or (not(x // 13 > 3)) or (x // a > 6)
        if f == False:
            return False
    return True

for a in range(1, 100):
    if f(a) == True:
        print(a)
        break
