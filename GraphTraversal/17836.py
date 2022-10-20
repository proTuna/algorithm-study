import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = []
n,m,t = map(int, input().rstrip().split())
for _ in range(n):
    l = list(map(int,input().rstrip().split()))
    graph.append(l)

visited = [[False]*m for _ in range(n)]
answer = int(1e9)
q = deque()
q.append((0,0,0))
visited[0][0] = True
while q:
    x,y,time = q.popleft()
    if x == n-1 and y == m-1:
        answer = min(answer,time)
        break
    if time+1>t:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if not visited[nx][ny]:
            if graph[nx][ny] == 1:
                continue
            elif graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx,ny,time+1))
            else:
                visited[nx][ny] == True
                tmp = time + 1 + abs(nx-(n-1)) + abs(ny-(m-1))
                if tmp<=t:
                    answer=min(answer,tmp)
if answer > t:
    print('Fail')
else:
    print(answer)