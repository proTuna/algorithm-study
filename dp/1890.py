import sys
input = sys.stdin.readline

n = int(input().rstrip())
b = [list(map(int,input().rstrip().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        right = j+b[i][j]
        bottom = i+b[i][j]
        if right<n:
            dp[i][right] += dp[i][j]
        if bottom<n:
            dp[bottom][j] += dp[i][j]

print(dp[n-1][n-1])