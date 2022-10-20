import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().rstrip().split())

MAX = 100001
answer = 0
visited = [False]*MAX
dist = [-1]*MAX
q = deque()
q.append(n)
dist[n] = 0
visited[n] = True

while q:
    now = q.popleft()
    if now*2 < MAX and visited[now*2] == False:
        q.appendleft(now*2)
        visited[now*2] = True
        dist[now*2] = dist[now]
    if now+1 < MAX and visited[now+1] == False:
        q.append(now+1)
        visited[now+1] = True
        dist[now+1] = dist[now]+1
    if now-1 >=0 and visited[now-1] == False:
        q.append(now-1)
        visited[now-1] = True
        dist[now-1] = dist[now]+1

print(dist[k])