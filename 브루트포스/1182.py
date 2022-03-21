import sys
input = sys.stdin.readline

n,s = map(int,input().rstrip().split())
l = list(map(int,input().rstrip().split()))
cnt = 0
def dfs(idx, total):
    global cnt
    if idx ==n:
        if total==s:
            cnt +=1
        return
    dfs(idx+1,total+l[idx])
    dfs(idx+1,total)

dfs(0,0)
if s == 0:
    cnt -=1

print(cnt)
