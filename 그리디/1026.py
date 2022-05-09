import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

a.sort()
b.sort(reverse=True)
answer = 0
for i in range(n):
    answer += a[i]*b[i]

print(answer)