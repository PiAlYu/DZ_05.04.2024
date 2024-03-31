m = -float('inf')
for x in range(16):
    for y in range(16):
        a = int('27a023', 16) + x * 16 ** 2
        b = int('80e5d2', 16) + y * 16 ** 4
        if (a + b) % 5 == 0:
            m = max(x + y, m)
print(m)