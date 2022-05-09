import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = 0

for i in range(1,n+1):
    tmp = str(i)
    if len(tmp) <3:
        answer+=1
    else:
        dif = int(tmp[1]) - int(tmp[0])
        for j in range(1,len(tmp)-1):
            dif_tmp = int(tmp[j+1]) - int(tmp[j])
            if dif_tmp != dif:
                break
        else:
            answer+=1

print(answer)