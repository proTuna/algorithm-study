import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
l = list(map(int,input().rstrip().split()))
l.sort()
dif = []

for i in range(n-1):
    dif.append(l[i+1]-l[i])

dif.sort()
print(sum(dif[:n-k]))