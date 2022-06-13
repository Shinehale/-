def check(val):
    val1=val**2
    val2=val**3
    S=[0]*10
    string=str(val1)
    for each in string:
        S[int(each)]+=1
    string=str(val2)
    for each in string:
        S[int(each)]+=1
    flag=True
    for i in range(10):
        if S[i]!=1:
            flag=False
    return flag

for i in range(1000):
    if check(i):
        print(i)
