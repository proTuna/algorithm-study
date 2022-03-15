from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())

q = deque()

for _ in range(n):
    query = input().split()
    if query[0] == 'push_front':
        q.appendleft(query[1])
    elif query[0] == 'push_back':
        q.append(query[1])
    elif query[0] == 'pop_front':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif query[0] == 'pop_back':
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(q))
    elif query[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif query[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)