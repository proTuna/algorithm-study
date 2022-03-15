import sys
input = sys.stdin.readline

A,B = map(int,input().rstrip().split())

a = set(list(map(int,input().rstrip().split())))
b = set(list(map(int,input().rstrip().split())))

dif = len(a) - len(a-b)

print(len(a)+len(b)-2*dif)