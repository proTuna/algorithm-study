import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().rstrip().split())
board = []
for _ in range(n):
    l = list(map(int,input().rstrip().split()))
    board.append(l)
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt+=1

answer = 0
tmp = []
while cnt>0:
    tmp.append(cnt)
    q = deque()
    q.append((0,0))
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not visited[nx][ny]:
                if board[nx][ny] == 1:
                    board[nx][ny] =0
                    visited[nx][ny] = True
                    cnt-=1
                elif board[nx][ny] ==0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    answer+=1

print(answer)
print(tmp[-1])
