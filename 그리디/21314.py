import sys
input = sys.stdin.readline

s = input().rstrip()

MIN = ''
s1 = []
for i in s:
    if i == 'M':
        s1.append(i)
    else:
        if len(s1)>0 and s1[-1] =='M' :
            MIN+=str(10**(len(s1)-1))
            s1 = []
            MIN+='5'
        else:
            MIN+='5'
if len(s1)>0:
    MIN += str(10**(len(s1)-1))

MAX = ''
s2 = []
for i in s:
    if i == 'M':
        s2.append(i)
    else:
        if len(s2)>0 and s2[-1] == 'M':
            MAX+=str(10**len(s2)*5)
            s2 = []
        else:
            MAX+='5'
if len(s2)>0:
    for _ in range(len(s2)):
        MAX +='1'
            

print(MAX)
print(MIN)