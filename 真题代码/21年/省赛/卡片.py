tot=[0 for i in range(10)]
ans=0
for i in range(100000000):
    value=str(i)
    flag=False
    for each in value:
        a=int(each)
        tot[a]+=1
        if tot[a]>2021:
            ans=i
            flag=True
            break
    if flag:
        break
print(ans-1)
