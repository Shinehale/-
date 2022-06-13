# 明显用dfs即可

import os
import sys

def dfs(pos,tot,a):# pos 表示已经到了第几个了，tot表示已经有的金钱，a表示挑选进的数组
    if pos==N:
        if tot==D_value:
            uni=tuple(a)
            if uni not in dt:
                for x in a:
                    print(x,end=" ")
                print("")
                dt.add(uni)
        return
    if tot+s[pos]<=D_value:
        a.append(s[pos])
        dfs(pos+1,tot+s[pos],a)
        a.pop()
    dfs(pos+1,tot,a)

Sum=int(input())
N=int(input())
s=[0 for i in range(N)]
for i in range(N):
    s[i]=int(input())
s.sort()
a=[]
dt=set()
sum=sum(s)
D_value=sum-Sum
dfs(0,0,a)

# 状态：1A