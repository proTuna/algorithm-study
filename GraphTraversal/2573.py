import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
N,M = map(int,input().rstrip().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(N)]

def findIce():
    newIce = set()
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                newIce.add((i,j))
    return newIce

def bfs(a,b,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
            elif graph[nx][ny] == 0:
                count[x][y] += 1

time = 0
while True:
    ice = findIce()
    cnt = 0
    if len(ice) == 0:
        print(0)
        break
    count = [[0]*M for _ in range(N)]
    visited = [[True]*M for _ in range(N)]
    for i,j in ice:
        visited[i][j] = False
    for i,j in ice:
        if not visited[i][j]:
            bfs(i,j,visited)
            cnt+=1
    for i in range(N):
        for j in range(M):
            graph[i][j] -= count[i][j]
            if graph[i][j] <0:
                graph[i][j] = 0
    if cnt>1:
        print(time)
        break
    time += 1