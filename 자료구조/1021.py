from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
l = list(map(int,input().rstrip().split()))

q = deque([i for i in range(1,n+1)])
cnt = 0
for i in l:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q)//2:
                q.rotate(-1)
                cnt+=1
            else:
                q.rotate(1)
                cnt+=1

print(cnt)