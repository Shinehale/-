import os
import sys

def check(s):
    value=int(s)
    if value%2012==0 and value%3==0 and value%12==0:
        return True
    else :
        return False
for i in range(1900,2000,1):
    for j in range(1,31,1):
        st=str(i)+'0'+str(6)
        if j>=10:
            st=st+str(j)
        else:
            st=st+'0'+str(j)
        # print(st)
        if check(st):
            print(st)
            break
