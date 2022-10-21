import sys
input = sys.stdin.readline
from collections import deque

dx = [0,-1,0,1,0,-1,-1,1,1]
dy = [0,0,1,0,-1,-1,1,1,-1]
graph = deque([list(input().rstrip()) for _ in range(8)])

q = deque()
q.append((7,0))
answer = 0
while q:
    visited = [[False]*8 for _ in range(8)]
    for _ in range(len(q)):
        x,y = q.popleft()
        if x == 0 and y == 7:
            print(1)
            exit(0)
        if graph[x][y] == '#':
            continue
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<8 and 0<=ny<8 and not visited[nx][ny] and graph[nx][ny] =='.':
                visited[nx][ny] = True
                q.append((nx,ny))
    graph.pop()
    graph.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

print(answer)