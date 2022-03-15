import heapq as hq

import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = []

for _ in range(n):
    n = int(input().rstrip())
    if n == 0:
        if len(a) == 0:
            print(0)
        else:
            print(hq.heappop(a)[1])
    else:
        hq.heappush(a, (abs(n),n))