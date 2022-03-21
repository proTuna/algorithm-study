import sys
input = sys.stdin.readline

def dfs(a, idx, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return
    if idx == len(a):
        return
    dfs(a, idx+1, lotto+[a[idx]])
    dfs(a, idx+1, lotto)

while True:
    n, *s = list(map(int,input().rstrip().split()))
    if n == 0:
        break
    dfs(s, 0, [])
    print()
