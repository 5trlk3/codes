#1
f = open('24.txt')
s = f.readline()
count = 0
s = s.replace('BIBA', '1')
s = s.replace('BOBA', '2')
for i in range(len(s) - 2):
    if s[i] == '1' and s[i + 2] == '2':
        count += 1
print(count)
