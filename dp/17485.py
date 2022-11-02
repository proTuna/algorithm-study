import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
board = [list(map(int,input().rstrip().split())) for _ in range(N)]
MAX = int(1e9)
dp = [[[MAX]*3 for _ in range(M)] for _ in range(N)]
for i in range(N):
    if i == 0:
        for j in range(M):
            for d in range(3):
                dp[i][j][d] = board[i][j]
    else:
        for j in range(M):
            if j == 0:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + board[i][j]
                dp[i][j][1] = dp[i-1][j][0] + board[i][j]
            elif j == M-1:
                dp[i][j][1] = dp[i-1][j][2] + board[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0],dp[i-1][j-1][1]) + board[i][j]
            else:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + board[i][j]
                dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + board[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0],dp[i-1][j-1][1]) + board[i][j]

answer = MAX
for i in range(M):
    answer = min(answer, min(dp[N-1][i]))
print(answer)