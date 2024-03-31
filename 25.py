from fnmatch import fnmatch

for i in range(21, 10 ** 9, 21):
    if fnmatch(str(i), '1*5*9'):
        s = str(i)
        if all(int(s[j]) > int(s[j - 1]) for j in range(1, len(s))):
            print(i, i // 21)