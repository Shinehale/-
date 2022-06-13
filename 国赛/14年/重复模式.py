def check(value):
    for i in range(N-value):
        m=R[i:i+value]
        pos=R.find(m,i+1)
        if pos>i:
            return True
    return False

R=str(input())
N=len(R)
lef,rig=0,N
while lef<=rig:
    mid=(lef+rig)>>1
    if check(mid):
        lef=mid+1
    else:
        rig=mid-1
if check(lef):
    print(lef)
elif check(lef-1):
    print(lef-1)