import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
b = [list(map(int,input().rstrip().split())) for _ in range(n)]
l = [list(map(int,input().rstrip().split())) for _ in range(m)]

prefix_sums = []
for i in range(n):
    sum_value = 0
    prefix_sum = [0]
    for j in b[i]:
        sum_value+=j
        prefix_sum.append(sum_value)
    prefix_sums.append(prefix_sum)

for i in l:
    x1,y1,x2,y2 = i
    s = 0
    for x in range(x1-1,x2):
        s += prefix_sums[x][y2] - prefix_sums[x][y1-1]
    print(s)