import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
a.sort()

answer = a[-1]
for i in range(n-1):
    answer += a[i]/2

print(answer)