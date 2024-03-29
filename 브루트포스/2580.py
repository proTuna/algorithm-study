from re import L
import sys
input = sys.stdin.readline

def square(x,y):
    return (x//3)*3+(y//3)

def go(z): # z 번째 칸을 채우는 함수 (x,y) -> 9*x+y번째 칸
    if z==81:
        for row in a:
            print(' '.join(map(str,row)))
        return True
    x = z//n
    y = z%n
    if a[x][y] !=0:
        return go(z+1)
    else:
        for i in range(1,10):
            if c1[x][i] == False and c2[y][i] == False and c3[square(x,y)][i] == False:
                c1[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                a[x][y] = 0
                c1[x][i] = c2[y][i] = c3[square(x,y)][i] = False
    return False

n = 9
a = [list(map(int,input().rstrip().split())) for _ in range(n)]
c1 = [[False]*10 for _ in range(n)] # c1[i][j] = i행에 숫자 j가 있으면  true
c2 = [[False]*10 for _ in range(n)] # c2[i][j] = i열에 숫자 j가 있으면 true
c3 = [[False]*10 for _ in range(n)] # c3[i][j] = i번 작은 정사각형에 숫자 j가 있으면 true
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c1[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i,j)][a[i][j]] = True
go(0)