ans=0
for i in range(1,30):
    for j in range(1,i):
        for k in range(1,j):
            if i**2+j**2+k**2==1000:
                ans=min(min(i,j),k)
                if ans==6:
                    continue
print(ans)