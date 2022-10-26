import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
N,M = map(int,input().rstrip().split())
graph=[list(map(int,input().rstrip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs(a,b):
    cnt = 1
    q = deque()
    q.append((a,b))
    visited[a][b] = num
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = num
                    q.append((nx,ny))
                    cnt+=1
    return cnt

# 인접한 1들을 그룹화 한다.
num = 1
group = dict()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i,j)
            group[num] = cnt
            num+=1

# 그리고 배열에서 0을 순차적으로 돌면서 배열에 인접한 1을 만날때 그 1이 어떤 그룹인지 확인하고 set에 넣어준다. 
# 만약, 중복된다면 넣어주지 않는다.
ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            s = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny] == 1 and visited[nx][ny] not in s:
                        s.add((visited[nx][ny]))
            res = 1
            for x in s:
                res+=group[x]
            ans = max(ans, res)
print(ans)
