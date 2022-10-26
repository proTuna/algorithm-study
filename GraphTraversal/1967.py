import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

for _ in range(n-1):
    s,e,w = map(int,input().rstrip().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))