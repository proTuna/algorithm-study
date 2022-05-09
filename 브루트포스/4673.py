import sys
input = sys.stdin.readline

s = set()

for i in range(1, 10001):
    tmp = str(i)
    for j in tmp:
        i+=int(j)
    s.add(i)

for i in range(1, 10001):
    if i not in s:
        print(i)