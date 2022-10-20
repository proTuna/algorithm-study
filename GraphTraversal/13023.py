import sys
input = sys.stdin.readline
from collections import defaultdict

def dfs(u,depth):
    global answer
    if depth == 4:
        answer = 1
        return
    for i in g[u]:
        if not checked[i]:
            checked[i] = 1
            dfs(i,depth+1)
            checked[i] = 0

n,m = map(int,input().rstrip().split())
g = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

answer = 0
checked = [0 for _ in range(n)]

for i in range(n):
    checked[i] = 1
    dfs(i,0)
    checked[i] = 0
    if answer:
        break

print(answer)