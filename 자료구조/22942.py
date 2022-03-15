import sys

input = sys.stdin.readline


class Point:
    def __init__(self,p,isOpen,no):
        self.p = p
        self.isOpen = isOpen
        self.no = no

def sol():
    n = int(input())
    c = []
    for i in range(n):
        x,r = map(int,input().rstrip().split())
        c.append(Point(x-r, True,i))
        c.append(Point(x+r,False,i))

    c.sort(key=lambda x : x.p)
    stack = []
    marked = set()
    for circle in c:
        cc = circle
        if cc.p in marked:
            print('NO')
            return
        if cc.isOpen:
            stack.append(cc)
            marked.add(cc.p)
        elif stack[-1].no != cc.no:
            print('NO')
            return
        else:
            marked.add(cc.p)
            stack.pop()
    print('YES')

if __name__=="__main__":
    sol()
