from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
g = [[] for _ in range(n+1)]
tmp = []
answer = []

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    g[b].append(a)

def bfs(start):
    q = deque([start])
    cnt = 1
    visited = [False for _ in range(n+1)]
    visited[start] = True
    
    while q:
        now = q.popleft()
        for i in g[now]:
            if not visited[i]:
                visited[i] = True
                cnt+=1
                q.append(i)
    return cnt

for i in range(1,n+1):
    cnt = bfs(i)
    tmp.append(cnt)

MAX = max(tmp)
for i,v in enumerate(tmp):
    if v == MAX:
        answer.append(i+1)

for i in answer:
    print(i,end=' ')
