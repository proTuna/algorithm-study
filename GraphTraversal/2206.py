import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,M = map(int,input().rstrip().split())
graph=[list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
# z를 추가해서 0은 안부숨 1 은 부숨으로 표현
# visited[x][y][0]은 안부순 경로, visited[x][y][1]은 부순 경로
def bfs(a,b):
    q =deque()
    q.append((a,b,0))
    visited[a][b][0] = 1
    while q:
        x,y,c = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # 벽이고 벽을 한번도 파괴하지 않은 경우
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[x][y][0] +1
                q.append((nx,ny,1))
            # 벽이 아니고 아직 한번도 방문하지 않은 경우
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] +1
                q.append((nx,ny,c))
    return -1

print(bfs(0,0))