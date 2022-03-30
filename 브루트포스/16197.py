import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().rstrip().split())
board = [list(input().rstrip()) for _ in range(n)]

def go(step, x1,y1,x2,y2):
    if step == 11:
        return -1
    c1 = False # 동전1이 떨어 졌는지 체크
    c2 = False # 동전2가 떨어 졌는지 체크
    if x1<0 or x1>=n or y1<0 or y1>=m:
        c1 = True
    if x2<0 or x2>=n or y2<0 or y2>=m:
        c2 = True
    if c1 and c2:
        return -1
    if c1 or c2:
        return step
    ans = -1
    for k in range(4):
        nx1, ny1 = x1+dx[k], y1+dy[k]
        nx2, ny2 = x2+dx[k], y2+dy[k]
        # 보드의 범위를 넘지 않고 벽이면
        if 0<=nx1<n and 0<=ny1<m and board[nx1][ny1] =='#':
            nx1, ny1 = x1,y1
        if 0<=nx2<n and 0<=ny2<m and board[nx2][ny2] =='#':
            nx2, ny2 = x2,y2
        tmp = go(step+1, nx1,ny1,nx2,ny2)
        if tmp == -1:
            continue
        if ans == -1 or ans>tmp:
            ans = tmp
    return ans

x1=y1=x2=y2=-1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            if x1 == -1:
                x1,y1 = i,j
            else:
                x2,y2 = i,j
            board[i][j] = '.' # 동전이 놓여있던 곳을 빈칸으로 바꿔준다.
print(go(0,x1,y1,x2,y2))