import sys
input = sys.stdin.readline

# 1
def dfs(s, goal):
    if s>goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1,4):
        now += dfs(s+i, goal)
    return now


t = int(input())
for _ in range(t):
    n = int(input())
    print(dfs(0,n))

# 2

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    dp = [0]*11
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])