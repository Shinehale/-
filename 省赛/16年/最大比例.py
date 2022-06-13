import math

N=int(input())
R=list(map(int,input().split()))
T=sorted(list(set(R)))
mx,ans=10000000,(0,0)
for i in range(len(T)-1):
    value=T[i+1]/T[i]
    if value<mx:
        mx=value
        gd=math.gcd(T[i+1] ,T[i])
        ans=(T[i+1]/gd,T[i]/gd)
print("%d/%d" %(int(ans[0]),int(ans[1])))
"""
9 
34878787205 887410625 22578125 261003125 6640625 10258466825 3017196125 118587876497 1953125
"""