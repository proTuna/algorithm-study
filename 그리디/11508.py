import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = [int(input().rstrip()) for _ in range(n)]
a = sorted(a, reverse=True)
answer = 0

for i in range(n):
    if (i+1)%3==0:
        continue
    answer+=a[i]

print(answer)