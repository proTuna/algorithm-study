import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = list(map(int,input().rstrip().split()))
c = [False]*(n*100000+10)
def dfs(idx, sum):
    if idx == n:
        c[sum] = True
        return
    dfs(idx+1, sum+s[idx])
    dfs(idx+1,sum)

dfs(0,0)
i = 1
while True:
    if c[i] == False:
        break
    i+=1
print(i)