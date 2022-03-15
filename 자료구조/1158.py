from collections import deque

n,k = map(int,input().split())

q = deque(list(range(1,n+1)))

ans = []

while len(q) != 0:
    q.rotate(-(k-1))
    ans.append(q.popleft())
    # for i in range(k-1):
    #     q.append(q.popleft())
    # ans.append(q.popleft())

print('<'+', '.join(map(str,ans))+'>')