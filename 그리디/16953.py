import sys
input = sys.stdin.readline

a,b = map(int,input().rstrip().split())
answer= -1

def go(s,e,c):
    global answer
    if s == e:
        answer = c
        return 
    if s>e:
        return
    else:
        go(s*2,e,c+1)
        go(s*10+1,e,c+1)
    return

go(a,b,0)

if answer > 0 :
    print(answer+1)
else:
    print(answer)