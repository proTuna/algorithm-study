import sys
input = sys.stdin.readline

def calc(row):
    if row == n:
        return 1
    ans = 0
    for i in range(n):
        if check(row,i):
            check_dig[row+i] = True
            check_dig2[row-i+n-1] = True
            check_col[i] = True
            a[row][i] = True
            ans+=calc(row+1)
            check_dig[row+i] = False
            check_dig2[row-i+n-1] = False
            check_col[i] = False
            a[row][i] = False
    return ans

def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True


n = int(input().rstrip())
a = [[False]*n for _ in range(n)]
check_col = [False]*n # i번 열에 퀸이 놓여져 있는지 여부
check_dig = [False]*(2*n-1) # / 방향 대각선에 퀸이 있는지 여부
check_dig2 = [False]*(2*n-1) # \ 방향 대각선에 퀸이 있는지 여부
print(calc(0))