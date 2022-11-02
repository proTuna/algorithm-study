import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = list(map(int,input().rstrip().split()))
dp = [[0]*21 for _ in range(N)]
# dp[idx번째][현재까지의 수] = 가능한 경우의 수
dp[0][l[0]] += 1

for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j+l[i] <=20:
                dp[i][j+l[i]] += dp[i-1][j]
            if j-l[i] >=0:
                dp[i][j-l[i]] += dp[i-1][j]

print(dp[N-2][l[-1]])