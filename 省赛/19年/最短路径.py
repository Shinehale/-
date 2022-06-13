import os

mp=[[]for i in range(21)]
vis=[0 for i in range(21)]
ans=100000
def dfs(pos,tot):
    if pos==20:
        global ans
        ans=min(ans,tot)
        return
    for to in mp[pos]:
        if vis[to[0]] : continue
        vis[to[0]]=1
        dfs(to[0],tot+to[1])
        vis[to[0]]=0

def add(s,t,len):
   mp[s].append((t,len))
   mp[t].append((s,len))

while True:
    try:
        R=input().split()
        s,t,len=int(R[0]),int(R[1]),int(R[2])
        add(s,t,len)
    except:
        break
dfs(1,0)
print(ans)