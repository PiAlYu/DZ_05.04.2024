fin = open('26.txt')
a = fin.readlines()
fin.close()
n, s = a.pop(0).split()
n, s = int(n), int(s)
a = [int(i) for i in a]
a.sort()
k, s0 = 0, s
for i in range(n):
    if a[i] < s:
        k += 1
        s -= a[i]
    else:
        print(k, s0)
        break