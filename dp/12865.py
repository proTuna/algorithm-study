import sys
input = sys.stdin.readline

N,K = map(int,input().rstrip().split())
bag = [[0,0]]
for _ in range(N):
    w,v = map(int,input().rstrip().split())
    bag.append([w,v])

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        w = bag[i][0]
        v = bag[i][1]

        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w]+v ,dp[i-1][j])

print(dp[N][K])