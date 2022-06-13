def calc(N):
    if N==1 :
        return 1
    if N==0:
        return 0
    ans=1
    for i in range(1,N+1,1):
        ans=ans*i
    return ans


S=input()
A=[]
for each in S:
    A.append(each)
A=sorted(A)
n=len(A)
dt={}
for i in range(len(S)):
    dt[A[i]]=i
ans=0
A=[]
for each in S:
    A.append(dt[each])
for i in range(n):
    tot=0
    for j in range(i+1,n):
        if A[i]>A[j]:
            tot+=1
    ans+=tot*calc(n-i-1)
print(ans)