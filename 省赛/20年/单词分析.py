import os
import sys

R=input()
length=len(R)
s=[0]*26
for i in range(length):
    pos=ord(R[i])-ord('a')
    s[pos]+=1
max,pos=s[0],0
for i in range(26):
    if (s[i] > s[pos]):
        pos=i
print(chr(ord('a')+pos))
print(s[pos])


