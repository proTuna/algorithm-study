import sys
import math
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
print(math.comb(n,m))