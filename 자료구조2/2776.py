import sys
input = sys.stdin.readline


# t = int(input().rstrip())

# for _ in range(t):
#     n1 = int(input().rstrip())
#     s1 = set(list(map(int,input().rstrip().split())))
#     n2 = int(input().rstrip())
#     s2 = list(map(int,input().rstrip().split()))
#     for i in s2:
#         if i in s1:
#             print(1)
#         else:
#             print(0)

def binary_search(target, start,end,arr):
    while start<=end:
        mid = (start+end)//2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

t = int(input().rstrip())
for _ in range(t):
    n1 = int(input().rstrip())
    s1 = list(map(int,input().rstrip().split()))
    s1.sort()
    n2 = int(input().rstrip())
    s2 = list(map(int,input().rstrip().split()))
    for i in s2:
        print(binary_search(i,0,n1-1,s1))