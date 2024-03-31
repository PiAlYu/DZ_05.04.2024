fin = open('24.txt')
s = fin.readline()
fin.close()
k, i, c = 0, 0, 0
while i < len(s):
    if s[i:i + 2] == 'EA':
        k += 2
        i += 2
    elif s[i:i + 3] == 'NPC':
        k += 3
        i += 3
    else:
        c = max(c, k)
        k = 0
        i += 1
print(c)