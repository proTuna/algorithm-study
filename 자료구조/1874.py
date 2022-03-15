import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = []
ans = []
cnt = 0
flag = True

for _ in range(n):
    t = int(input())

    while cnt < t:
        cnt +=1
        s.append(cnt)
        ans.append('+')
    
    if s[-1] == t:
        s.pop()
        ans.append('-')
    else:
        flag = False
        break

if flag:
    for op in ans:
        print(op)
else:
    print('NO')