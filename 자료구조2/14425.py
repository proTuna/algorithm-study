import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
_set = set()
cnt = 0

for _ in range(n):
    s = input().rstrip()
    _set.add(s)

for _ in range(m):
    s = input().rstrip()
    if s in _set:
        cnt+=1
    else:
        continue
print(cnt)