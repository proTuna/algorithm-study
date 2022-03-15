from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())

q = deque(list(range(1,n+1)))

while len(q)>1:
    q.popleft()
    q.rotate(-1)

print(q[0])