import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int,input().rstrip().split()))

dp = [0]*n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j]< a[i] and dp[j]+1> dp[i]:
            dp[i] = dp[j] +1

print(max(dp))