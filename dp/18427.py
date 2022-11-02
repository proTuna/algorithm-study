import sys
input = sys.stdin.readline

N,M,H = map(int,input().rstrip().split())
boxes = [list(map(int,input().rstrip().split())) for _ in range(N)]
dp =[0]*(H+1)

for box in boxes:
    for i in range(H,0,-1):
        if not dp[i]:
            continue
        for num in box:
            if i+num>H:
                continue
            dp[i+num] += dp[i]
    for num in box:
        dp[num] += 1

print(dp[H]%10007)
