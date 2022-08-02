import sys
n,m = map(int,input().split())

check = [False]*(n+1)
a = [0]*m

def go(index,start,n,m):
    if index ==m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start,n+1):
        a[index] = i
        go(index+1,i,n,m)

go(0,1,n,m)