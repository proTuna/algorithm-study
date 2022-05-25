import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n,m = map(int,input().rstrip().split())
    print(math.comb(m,n))
