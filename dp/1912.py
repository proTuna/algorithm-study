import sys
input = sys.stdin.readline

n = int(input().rstrip().split())
l = list(map(int,input().rstrip().split()))

dp = [0]*n
for i in range(n):
    dp[i] = l[i]
    if i == 0 : continue
    if dp[i] < dp[i-1] + l[i]:
        dp[i] = dp[i-1] + l[i]

print(max(dp))