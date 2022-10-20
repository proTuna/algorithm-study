import sys
input = sys.stdin.readline
from collections import defaultdict


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for i in l[u]:
        if i not in visited:
            dfs(i, visited.copy())
        else: # 사이클이 생기면 뽑는다.
            answer.extend(list(visited))
            return

n = int(input().rstrip())
l = defaultdict(list)
for i in range(1,n+1):
    v = int(input().rstrip())
    l[v].append(i)

checked = [0 for _ in range(n+1)]
answer = []
for i in range(1,n+1):
    if not checked[i]:
        dfs(i,set([]))

answer.sort()
print(len(answer))
for i in answer:
    print(i)