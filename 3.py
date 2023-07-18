#3
f = open('24.txt')
s = f.readline()
count = 0

for i in range(len(s) - 1):
    first = str(ord(s[i]))
    second = str(ord(s[i + 1]))
    what = first + second
    f = 0
    for j in range(len(what) // 2):
        if what[j] != what[len(what) - 1 - j]:
            f = 1
    if f == 0:
        count += 1
print(count)