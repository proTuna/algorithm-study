import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = [0]
dp = [0]*(n+1)
for _ in range(n):
    a.append(int(input().rstrip()))

dp[1] = a[1]
if n>=2:
    dp[2] = a[1]+a[2]

for i in range(3,n+1):
    dp[i] = dp[i-1]
    dp[i] = max(dp[i-2]+a[i], dp[i])
    dp[i] = max(dp[i-3]+a[i-1]+a[i],dp[i])

print(dp[n])