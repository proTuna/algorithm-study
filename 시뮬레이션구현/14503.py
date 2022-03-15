import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().rstrip().split())
x,y,d = map(int,input().rstrip().split())
a = [list(map(int,input().rstrip().split())) for _ in range(n)]
cnt = 0

while True:
    if a[x][y] == 0:
        a[x][y] = 2
    if a[x+1][y] != 0 and a[x-1][y] != 0 and a[x][y-1] != 0 and a[x][y+1] != 0:
        if a[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x -= dx[d]
            y -= dy[d]
    else:
        d = (d+3)%4
        if a[x+dx[d]][y+dy[d]] == 0:
            x+=dx[d]
            y+=dy[d]

for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            cnt+=1

print(cnt)