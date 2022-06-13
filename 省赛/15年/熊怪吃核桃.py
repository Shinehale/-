N=1543
ans=0
while N:
    if N%2:
        new_=1
        N-=1
    else:
        new_=0
    ans+=new_
    N=N//2
print(ans)
# 1A