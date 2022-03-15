import heapq as hq
import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    max_q = []
    min_q = []
    for _ in range(k):
        query = input().split()
        if query[0] == 'I':
            if int(query[1]) >0:
                hq.heappush(max_q,-int(query[1]))
            else:
                hq.heappush(min_q,int(query[1]))
        else:
            if int(query[1]) == 1 and len(max_q)>0:
                hq.heappop(max_q)
            elif int(query[1]) == -1 and len(min_q) > 0:
                hq.heappop(min_q)
    
    if len(max_q) > 0 and len(min_q) >0:
        print('%s %s'%(-hq.heappop(max_q),hq.heappop(min_q)))
    elif len(max_q) == 0 or len(min_q) == 0:
        print('EMPTY')