ans=0
def check(val):
    flag=True
    string=str(val)
    for each in string:
        if each=='4':
            flag=False
    return flag
for i in range(10000,99999+1):
    if check(i):
        ans+=1
print(ans)