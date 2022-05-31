import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
coines = [int(input().rstrip()) for _ in range(n)]

dp = [0 for i in range(k+1)]
dp[0] = 1

for i in range(n):
    for j in range(coines[i],k+1):
        if j-coines[i]>=0:
            dp[j] += dp[j-coines[i]]

print(dp[k])