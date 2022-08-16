import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
l = list(map(int,input().rstrip().split()))
l.sort()
a = [0]*m

def go(index,n,m):
    if index ==m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        a[index] = l[i]
        go(index+1,n,m)
        
go(0,n,m)