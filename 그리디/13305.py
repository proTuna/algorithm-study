import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int,input().rstrip().split()))
p = list(map(int,input().rstrip().split()))

answer = 0
now_price = p[0]
for i in range(n-1):
    if p[i] < now_price:
        now_price = p[i]
    answer += now_price*l[i]

print(answer)