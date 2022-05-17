import sys
import heapq as hq
input = sys.stdin.readline

n = int(input().rstrip())
c = [tuple(map(int,input().rstrip().split())) for _ in range(n)]
c.sort()
heap = []
hq.heappush(heap, c[0][1])

for i in range(1, n):
    if c[i][0] < heap[0]:
        hq.heappush(heap, c[i][1])
    else:
        hq.heappop(heap)
        hq.heappush(heap, c[i][1])

print(len(heap))