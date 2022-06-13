p=[0 for x in range(60)]
for i in range(1,60):
    if i %2:
        p[i]=1
    else:
        p[i]=0
ans=0
for i in range(21,51):
    ans+=p[i]
print(ans)
# 1A
