import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = []
n,m = map(int,input().rstrip().split())
for _ in range(n):
    l = list(map(int,input().rstrip().split()))
    graph.append(l)

target_x, target_y = 0,0
is_find = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            target_x = i
            target_y = j
            is_find = True
            break
    if is_find:
        break

tmp = [[-1 for _ in range(m)] for _ in range(n)] # 방문 할 수 없는 곳은 -1
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            tmp[i][j] = 0

q = deque()
q.append((target_x,target_y))
tmp[target_x][target_y] = 0
visited[target_x][target_y] = True
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny] ==1 and visited[nx][ny] == False:
            tmp[nx][ny] = tmp[x][y] +1
            visited[nx][ny] = True
            q.append((nx,ny))

for i in tmp:
    print(' '.join(map(str,i)))