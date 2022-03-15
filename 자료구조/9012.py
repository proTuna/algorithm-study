import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    ps = [s for s in input().rstrip()]
    stack = []
    stack.append(ps[0])
    for i in range(1,len(ps)):
        if len(stack) == 0:
            stack.append(ps[i])
            continue
        if stack[-1] == '(' and ps[i] == ')':
            stack.pop()
        else:
            stack.append(ps[i])
    if len(stack):
        print('NO')
    else:
        print('YES')