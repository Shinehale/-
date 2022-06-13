import os
import sys

# 请在此输入您的代码
w=eval(input())
fs=[1,3,9,27,81]
vis=[False]*5
res=[0]*5
rest=[]
def dfs(step,num):
    global res,rest
    if num==w:
        rest=res.copy()
        return
    if step==5:
        return
    for i in range(-1,2):
        res[step]=i
        dfs(step+1,num+fs[step]*i)
        res[step]=0
dfs(0,0)
strres=''
for i in range(4,-1,-1):
    if rest[i]==0:
        continue
    if rest[i]==1:
        strres+='+'
    else:
        strres+='-'
    strres+=str(fs[i])
print(strres[1:])