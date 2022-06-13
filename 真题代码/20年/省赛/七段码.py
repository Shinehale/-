import sys
import os
import math

ans = 0
_set = {(0,5),(0,1),(1,6),(1,2),(2,3),(3,4),(4,5),(5,6),(4,6),(2,6)}
ls = [0 for i in range(7)]

# def out_print(ls):
#     if ls[0]==1:print("---")
#     else:print(" ")
#     if ls[5]==0:print(" ",end=" ")
#     else:print("|",end=" ")
#     if ls[1]==0:print(" ")
#     else:print("|")
#     if ls[6]==1:print("---")
#     else:print(" ")
#     if ls[4]==0:print(" ",end=" ")
#     else:print("|",end=" ")
#     if ls[2]==0:print(" ")
#     else:print("|")
#     if ls[3]==1:print("---")
#     else:print(" ")

def check(ls):
    flag = True
    tot=[0 for i in range(7)]
    for i in range(7):
        for j in range(7):
            if ls[i] != 1 or ls[j] != 1: continue
            if i == j: continue
            if (i, j)  in _set or (j, i)  in _set:
                tot[i]+=1
                tot[j]+=1
    for i in range(7):
        if ls[i]==1 and tot[i]==0 :
            flag=False
    if sum(ls)==1:flag=True
    if flag:
        global ans
        ans += 1
        # out_print(ls)
        # print(ls)


def dfs(ls, pos):
    if pos == 7:
        check(ls)
        return
    ls[pos] = 1
    dfs(ls, pos + 1)
    ls[pos] = 0
    dfs(ls, pos + 1)


dfs(ls, 0)
print(ans - 4)
"""
| |
 
| |
 
[0, 1, 1, 0, 1, 1, 0]
---
|  
 
  |
---
[1, 0, 1, 1, 0, 1, 0]
---
  |
 
|  
---
[1, 1, 0, 1, 1, 0, 0]
上述是三种特别情况
是这个代码无法判断出来的
要是想完全解决需要使用并查集来处理
"""