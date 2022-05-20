import sys
import heapq as hq
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    k = int(input().rstrip())
    l = list(map(int,input().rstrip().split()))
    hq.heapify(l)
    answer = 0
    while True:
        if len(l) == 1:
            break
        a = hq.heappop(l)
        b = hq.heappop(l)
        answer += a+b
        hq.heappush(l,a+b)
    print(answer)