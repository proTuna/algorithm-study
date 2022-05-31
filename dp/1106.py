import sys
input = sys.stdin.readline

c,n = map(int,input().rstrip().split())
p = []
for _ in range(n):
    price, customer = map(int,input().rstrip().split())
    p.append([price,customer])

p.sort()
dp = [int(1e9)]*1101
dp[0] = 0

for i in range(len(p)):
    for j in range(p[i][1],1101):
        dp[j] = min(dp[j], dp[j-p[i][1]]+p[i][0])

print(min(dp[c:]))