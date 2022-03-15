import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,m,x,y,k = map(int,input().rstrip().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().rstrip().split())))

cmd = list(map(int,input().rstrip().split()))

dice = [0]*7

for c in cmd:
    c-=1
    nx,ny = x+dx[c], y+dy[c]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    if c == 0:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    elif c == 1:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
    elif c == 2:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
    else:
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp
    x,y = nx,ny
    if a[x][y] == 0:
        a[x][y] = dice[6]
    else:
        dice[6] = a[x][y]
        a[x][y] =0
    print(dice[1])