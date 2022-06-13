def res(S):
    ret=''
    for i in range(len(S)-1,-1,-1):
        ret+=(S[i])
    return ret

def judge(S):
    flag=True
    for i in range(len(S)//2):
        if S[i]!=S[len(S)-i-1]:
            flag=False
    return flag

def check(num):
    step=0
    while step<=30:
        step+=1
        string=str(num)
        Tar=res(string)
        num+=int(Tar)
        if judge(str(num)):
            break
    return not judge(str(num))


for i in range(1,201):
    if check(i):
        print(i)