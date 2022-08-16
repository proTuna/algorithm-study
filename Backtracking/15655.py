import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
l = list(map(int,input().rstrip().split()))
l.sort()
check = [False]*(n)
a = [0]*m

def go(index,start,n,m):
    if index ==m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start,n):
        if check[i]:
            continue
        check[i] = True
        a[index] = l[i]
        go(index+1,i+1,n,m)
        check[i] = False

go(0,0,n,m)