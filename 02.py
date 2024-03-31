print('          x y z f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = not(x == (y <= z))
            s = str(x) + str(y) + str(z)
            if f == 1 and s.count('1') == 1:
                print('1 строка:', x, y, z, f)
            if f == 0 and s.count('1') == 2:
                print('2 строка:', x, y, z, f)