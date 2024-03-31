a, b = float('inf'), 0
for n in range(1, 100):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + '010'
    else:
        r = r + bin(5 * (n % 3))[2:]
    r = int(r, 2)
    if r > 300:
        if r < a and r % 2 == 0:
            a = r
            b = n
print(b)