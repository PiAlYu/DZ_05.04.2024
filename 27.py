fin = open('27B.txt')
a = fin.readlines()
fin.close()
a.pop(0)
a = [int(i) for i in a]
mi = float('inf')
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 144 == 0 and a[i] < a[j]:
            mi = min(mi, a[i] + a[j])
print(mi)
# Оно работает для двух файлов!
