import math
ans=0
for i in range(10,100,1):
    s=str(i)
    string=s[1]+s[0]
    new=int(string)
    if i-new==27:
        ans+=1
print(ans)
