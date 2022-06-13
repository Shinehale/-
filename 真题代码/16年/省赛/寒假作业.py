import itertools

def check(Lis):
    if Lis[0]+Lis[1]==Lis[2] and Lis[3]-Lis[4]==Lis[5] and\
        Lis[6]*Lis[7]==Lis[8] and Lis[11]*Lis[10]==Lis[9]:
        return True
    else:
        return False
lis=list(itertools.permutations([i for i in range(1,14)]))
ans=0
for each in lis:
    if check(each):
        print(each)
        ans+=1
print(ans)