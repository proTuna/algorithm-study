import sys
input = sys.stdin.readline
from collections import deque
import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = -int(1e9)
n,m = map(int,input().rstrip().split())
r = []
for _ in range(n):
    r.append(list(map(int,input().rstrip().split())))

def dfs(l):
    if l == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if r[i][j] == 0:
                    r[i][j] = 1
                    dfs(l+1)
                    r[i][j] =0


def bfs():
    global answer
    q = deque()
    tmp = copy.deepcopy(r)
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i,j))
    while q:
        x,y  = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt+=1
    answer = max(answer,cnt)

dfs(0)
print(answer)