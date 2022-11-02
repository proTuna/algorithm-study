import sys
input = sys.stdin.readline

T = int(input().rstrip())
k = int(input().rstrip())
coines = [[0,0]]
for _ in range(k):
    coines.append(list(map(int,input().rstrip().split())))

dp = [0]*(T+1)
dp[0] = 1
for coin,cnt in coines:
    for money in range(T,0,-1): # T원부터 1원까지
        for i in range(1,cnt+1):
            if money-coin*i >= 0:
                dp[money] += dp[money-coin*i]

print(dp[T])