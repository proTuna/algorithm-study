import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
R,C = map(int,input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(R)]
q = deque()

# 지훈이를 먼저 이동시키고나서 불을 이동시키면 된다.
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            q.append((i,j,0))
            break

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            q.append((i,j,-1))
answer = "IMPOSSIBLE "

while q:
    x,y,time = q.popleft()
    # 종료 조건
    if time>-1 and graph[x][y] !='F' and (x==0 or y==0 or x==R-1 or y==C-1):
        answer=time+1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and graph[nx][ny] != '#': 
            # 지훈이 이동
            if time>-1 and graph[nx][ny] =='.':
                graph[nx][ny] = '_'
                q.append((nx,ny,time+1))
            # 불 이동
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append((nx,ny,-1))

print(answer)