import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,M = map(int,input().rstrip().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
walls = set()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            walls.add((i,j))
H,W,sr,sc,fr,fc = map(int,input().rstrip().split())

def bfs(a,b):
    q = deque()
    q.append((a,b,0))
    visited[a][b] = True
    while q:
        x,y,cnt = q.popleft()
        if x == fr-1 and y == fc-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx and nx+H-1<N and 0<=ny and ny+W-1<M and not visited[nx][ny] and check(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return -1

def check(a,b):
    for i,j in walls:
        if a<=i<a+H and b<=j<b+W:
            return False
    return True

print(bfs(sr-1,sc-1))