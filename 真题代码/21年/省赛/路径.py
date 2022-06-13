import math
import queue
INF=214748364741515151515

def SPFA(x):
    que=queue.Queue()
    for i in range(N):
        dis[i]=INF
    dis[x]=0
    inque[x]=True
    que.put(x)
    while not que.empty():
        x=que.get()
        inque[x]=False
        for each in G[x]:
            y,dist=each[0],each[1]
            if dis[y]>dis[x]+dist:
                dis[y]=dis[x]+dist
                if not inque[y]:
                    que.put(y)
                    inque[y]=True
    return dis[2020]
N=2021
dis,inque=[0]*N,[False]*N
G={}
for i in range(N):
    G[i]=[]
for i in range(N):
    for j in range(i):
        if i==j :
            continue
        if abs(i-j)>21:
            continue
        dist=(i+1)*(j+1)//math.gcd(i+1,j+1)
        G[i].append((j,dist))
        G[j].append((i,dist))
ans=SPFA(0)
print(ans)
