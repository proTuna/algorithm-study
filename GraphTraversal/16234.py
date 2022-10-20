import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,L,R = map(int, input().rstrip().split())
country=[]
for _ in range(N):
    l = list(map(int, input().rstrip().split()))
    country.append(l)

def bfs(a,b):
    q = deque()
    tmp = []
    q.append((a,b))
    tmp.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N and visited[nx][ny]==0:
                if L <= abs(country[nx][ny] - country[x][y]) <=R:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    tmp.append((nx,ny))
    return tmp

answer = 0

while True:
    visited = [[False]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                l = bfs(i,j)
                if len(l) >1:
                    flag = 1
                    move = sum([country[x][y] for x,y in l])//len(l)
                    for x,y in l:
                        country[x][y] = move
    # 인구 이동이 일어나지 않는다면 break
    if flag == 0:
        break
    answer+=1

print(answer)