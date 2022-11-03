import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]

# 가장 긴 증가하는 부분수열을 이용한다.
dp = [0]*N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if arr[j]< arr[i] and dp[j]+1> dp[i]:
            dp[i] = dp[j] +1

print(N-max(dp))