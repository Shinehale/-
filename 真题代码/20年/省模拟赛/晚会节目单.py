S=[]
ans=[]
R=list(map(int,input().split()))
N,M=R[0],R[1]
R=list(map(int,input().split()))
for i in range(N):
    pos=i
    S.append((R[i],i))
S.sort(key=lambda x:(-x[0]))
for i in range(M):
    pos=S[i][1]
    ans.append(pos)
ans.sort()
for item in ans:
    print(R[item],end=" ")
"""
10 7 
15 56 59 41 69 66 6 76 15 50
"""