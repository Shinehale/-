tot=0
for i in range(1,1000):
    k=i**3
    for j in range(1,4):
        p=k%(10**j)
        if p==i:
            tot+=1
            continue
print(tot)