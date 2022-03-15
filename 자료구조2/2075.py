import heapq as hq

import sys
input = sys.stdin.readline

n = int(input().rstrip())

a = []

for _ in range(n):
    l = list(map(int, input().rstrip().split()))
    for i in l:
        hq.heappush(a, i)

    while len(a) > n:
        hq.heappop(a)

print(hq.heappop(a))