import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
c = []
dp = [int(1e9)]*10001
dp[0] = 0
for _ in range(n):
    coin = int(input().rstrip())
    c.append(coin)

for i in range(len(c)):
    for j in range(c[i],k+1):
        dp[j] = min(dp[j],dp[j-c[i]]+1)

if dp[k] == int(1e9):
    print(-1)
else:
    print(dp[k])