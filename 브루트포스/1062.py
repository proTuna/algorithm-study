# 26개의 알파벳 중에서 K개를 고르고
# N개의 단어 중에서 고른 알파벳으로 이루어진 단어의 개수를 구한다.
# a, n, c, i, t는 필수로 포함하므로 K-5개를 고른다.

import sys
input = sys.stdin.readline
# 이렇게 하면 시간초과
# def count(words):
#     cnt = 0
#     for word in words:
#         flag = True
#         for x in word:
#             if not learn[ord(x)-ord('a')]:
#                 flag = False
#                 break
#         if flag:
#             cnt+=1
#     return cnt

# def go(index, k, words):
#     if k < 0:
#         return 0
#     if index == 26:
#         return count(words)
#     ans = 0
#     # 현재 알파벳을 고른 경우
#     learn[index] = True
#     t1 = go(index+1, k-1, words)
#     learn[index] = False
#     # 고르지 않은 경우
#     if ans < t1:
#         ans = t1
#     if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
#         t2 = go(index+1, k, words)
#         if ans < t2:
#             ans = t2
#     return ans

# n,m = map(int,input().rstrip().split())
# words = [input().rstrip() for _ in range(n)]
# learn = [False]*26

def count(mask,words):
    cnt = 0
    for word in words:
        if(word & ((1<<26)-1-mask)) == 0:
            cnt+=1
    return cnt

def go(index, k, mask, words):
    if k < 0:
        return 0
    if index == 26:
        return count(mask, words)
    ans = 0
    t1 = go(index+1, k-1, mask | (1<<index), words)
    if ans < t1:
        ans = t1
    if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
        t2 = go(index+1, k, mask, words)
        if ans < t2:
            ans = t2
    return ans


n,m = map(int,input().split())
words = [0] * n
for i in range(n):
    s = input().rstrip()
    for x in s:
        words[i] |= (1 << (ord(x)-ord('a')))
print(go(0,m,0,words))

