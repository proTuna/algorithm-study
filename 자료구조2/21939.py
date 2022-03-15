import heapq as hq
import sys
input = sys.stdin.readline

n = int(input().rstrip())

min_q = []
max_q = []

for _ in range(n):
    P, L = map(int,input().rstrip().split())
    hq.heappush(min_q, [L,P])
    hq.heappush(max_q [-L,-P])

m = int(input().rstrip())

for _ in range(m):
    query = input().rstrip().split()

    # if query[0] == 'add':
    #     # do something
    # elif query[0] == 'recommend':
    #     if query[1] == '1':
    #         #do something
    #     else:

    #     # do something
    # elif query[0] == 'solved':
    #     # do something