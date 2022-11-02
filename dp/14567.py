import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().rstrip().split())
graph = [[] for _ in range(N+1)]
q = deque()
indgree = [0]*(N+1)
cur = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    indgree[b]+=1

for i in range(1,N+1):
    if indgree[i] == 0:
        q.append((i,1))
        cur[i] = 1

while q:
    s, cnt = q.popleft()
    for i in graph[s]:
        indgree[i]-=1
        if indgree[i] ==0:
            q.append((i,cnt+1))
            cur[i] = cnt+1

print(*cur[1:])