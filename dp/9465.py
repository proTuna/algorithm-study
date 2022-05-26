import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    l = []
    for _ in range(2):
        l.append(list(map(int,input().rstrip().split())))
    for i in range(1,n):
        if i == 1:
            l[0][i] += l[1][i-1]
            l[1][i] += l[0][i-1]
        else:
            l[0][i] += max(l[1][i-1],l[1][i-2])
            l[1][i] += max(l[0][i-1],l[0][i-2])
    print(max(l[0][n-1],l[1][n-1]))