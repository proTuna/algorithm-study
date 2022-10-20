import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().rstrip().split())
l = list(map(int,input().rstrip().split()))
visit = set()

q = deque()
for i in l:
    q.append((i,1))
    visit.add(i)

answer = 0
n_b = 0

while q:
    now,b = q.popleft()
    for i in [-1,1]:
        nx = now + i
        if nx in visit:
            continue
        visit.add(nx)
        answer += b
        n_b += 1
        q.append((nx,b+1))
        if n_b == k:
            q =deque()
            break
print(answer)