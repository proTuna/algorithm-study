import sys

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

_dict = {}

for i in range(1,n+1):
    poketmon = input().rstrip()
    _dict[i] = poketmon
    _dict[poketmon] = i

for _ in range(m):
    prob = input().rstrip()
    if prob.isdigit():
        print(_dict[int(prob)])
    else:
        print(_dict[prob])
