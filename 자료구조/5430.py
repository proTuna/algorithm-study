from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    ls = input().rstrip()
    l = []
    if n >0:
        l = list(map(int,ls[1:-1].split(',')))
    ans = deque(l)
    p.replace('RR','')
    reverse = 0
    for i in p:
        if i == 'R':
            reverse+=1
        elif i == 'D':
            if len(ans)<1:
                print('error')
                break
            else:
                if reverse%2==0:
                    ans.popleft()
                else:
                    ans.pop()
    else:
        if reverse%2==0:
            print('['+ ','.join(map(str, ans))+']')
        else:
            ans.reverse()
            print('['+ ','.join(map(str, ans))+']')
