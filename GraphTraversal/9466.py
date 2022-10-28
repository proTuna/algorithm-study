import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n):
    global answer
    visited[n] = True
    cycle.append(n)
    num = l[n]
    if visited[num]:
        if num in cycle:
            answer += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

T = int(input().rstrip())
for _ in range(T):
    answer = []
    N = int(input().rstrip())
    visited = [False]*(N+1)
    l = [0]+list(map(int,input().rstrip().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(N):
        if not visited[i+1]:
            cycle = []
            dfs(i+1)
    print(N-len(answer))
