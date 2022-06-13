# 单纯的模拟
import os
import sys


def check(s):
    if s>='a' and s<='z':
        return 1
    else:
        return 0


def check_n(s):
    if s>='0' and s<='9':
        return 1
    else:
        return 0


S=input()
ans=""

if check(S[0]):
    ans+=chr(ord(S[0])-32)
elif check_n(S[0]):
    ans+=S[0]
for i in range(1,len(S),1):
    if S[i]==' ' and S[i-1]==' ':
        continue
    if check(S[i]) and check_n(S[i-1]):
        ans+="_"+S[i]
    elif check_n(S[i]) and check(S[i-1]):
        ans+="_"+S[i]
    elif check(S[i]) and S[i-1]==' ':
        ans+=chr(ord(S[i])-32)
    else:
        ans+=S[i]
print(ans)


# you and me what      cpp2005program