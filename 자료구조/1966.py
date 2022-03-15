from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n,w = map(int,input().split())
    l = list(map(int,input().split()))
    q = []
    for idx,val in enumerate(l):
        q.append([val,idx])
    q = deque(q)
    cnt = 0
    while True:
        v = q.popleft()
        if any(v[0]<x[0] for x in q):
            q.append(v)
        else:
            cnt+=1
            if v[1] == w:
                print(cnt)
                break

