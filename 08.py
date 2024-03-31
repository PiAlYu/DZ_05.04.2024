from itertools import product
k, c = 0, 0
for i in product('ЬРПЛЕА', repeat = 5):
    k += 1
    if i[-1] == 'Ь':
        c += 1
    if k == 387:
        break
print(c)