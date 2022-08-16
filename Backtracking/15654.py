import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
l = list(map(int,input().rstrip().split()))
l.sort()
check = [False]*(n)
a = [0]*m

def go(index,n,m):
    if index ==m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        a[index] = l[i]
        go(index+1,n,m)
        check[i] = False

go(0,n,m)