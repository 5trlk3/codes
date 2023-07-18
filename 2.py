#2
f = open('24.txt')
s = f.readline()
count = 0
s = s.replace('ТЯГИ', '*')
for i in range(len(s)):
    if s[i] == '*':
        kol += 1
        if kol == 2:
            count += 1
            kol -= 1
print(count)