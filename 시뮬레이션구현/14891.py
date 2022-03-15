import sys
input = sys.stdin.readline

n = 4
a = [list(input().rstrip()) for _ in range(n)]
k = int(input().rstrip())
for _ in range(k):
    no, dir = map(int,input().rstrip().split()) # 어떤 톱니바퀴를 어디로 돌릴지
    no -=1
    d = [0]*n # 톱니바퀴들의 회전 방향을 결정
    d[no] = dir
    for i in range(no-1,-1,-1): # 왼쪽 톱니를 연쇄적으로 구함
        if a[i][2] != a[i+1][6]:
            d[i] = -d[i+1]
        else:
            # 한 톱니가 회전하지 않으면 그 톱니에 있는 톱니도 회전하지 않는다.
            break
    for i in range(no+1, n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break
    for i in range(n):
        if d[i] == 0:
            continue
        if d[i] == 1:
            tmp = a[i][7]
            for j in range(7,0,-1):
                a[i][j] = a[i][j-1]
            a[i][0] = tmp
        elif d[i] == -1:
            tmp = a[i][0]
            for j in range(0,7):
                a[i][j] = a[i][j+1]
            a[i][7] = tmp
ans = 0
for i in range(n):
    if a[i][0] == '1':
        ans |= (1 << i)
print(ans)