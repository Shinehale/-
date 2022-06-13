import math
dt={}
for i in range(1,16):
    dt[i]=chr(ord('a')+i-1)
ans=[10,15,14,13,12,11,9,8,7,6,5,4,3,2,1]
for each in ans:
    print(dt[each],end="")

