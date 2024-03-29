import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
LOG = 21 # 2^20 = 1,000,000
t = int(input().rstrip())

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        dfs(y, depth+1)

# 전체 부모 관계를 설정하는 함수
def set_parent(root):
    dfs(root,0)
    for i in range(1, LOG):
        for j in range(1,n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # b가 더 깊도록 설정
    if d[a]>d[b]:
        a,b = b,a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG-1,-1,-1):
        if d[b]-d[a]>=(1<<i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG-1,-1,-1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

for _ in range(t):
    n = int(input().rstrip())

    parent =[[0]*LOG for _ in range(n+1)] # 부모 노드 정보
    d = [0]*(n+1) # 각 노드까지의 깊이
    c = [0]*(n+1) # 각 노드의 깊이가 계산되어있는지 여부
    graph = [[] for _ in range(n+1)] # 그래프 정보

    for _ in range(n-1):
        a,b = map(int,input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
        parent[b][0] = a

    start = 0
    for i in range(1,n+1):
        if parent[i][0] == 0:
            start = i

    set_parent(start)

    a,b = map(int, input().rstrip().split())
    print(lca(a,b))
