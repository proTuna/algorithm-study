from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
g = [[] for _ in range(n+1)]
p = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int , input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

def bfs():
    q = deque()
    q.append(1)

    while q:
        node = q.popleft()
        for i in g[node]:
            if p[i] == 0:
                p[i] = node
                q.append(i)

bfs()

for i in range(2,n+1):
    print(p[i])

