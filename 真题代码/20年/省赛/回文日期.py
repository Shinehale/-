import os
import sys

dt={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def jud(s):
    if s%400==0 or s%100!=0 and s%4==0 :
        return True
    else:
        return False
def check_year(s):
    if jud(s):
        dt[2]=29
    else:
        dt[2]=28
    ss=str(s)
    month=int(ss[3]+ss[2])
    day=int(ss[1]+ss[0])
    if month>12 or month==0:
        return None
    elif day>dt[month]:
        return None
    else:
        return ss+ss[3]+ss[2]+ss[1]+ss[0]

R=input()
year,month,day=R[0:4],R[4:6],R[6:8]
p=check_year(int(year))
if p==None :
    start=int(year)+1
elif int(p[4:6])<int(month) or int(p[4:6])==int(month) and int(p[6:8])<=int(day):
    start=int(year)+1
else:
    start=int(year)
for i in range(start,9999,1):
    ans=check_year(i)
    if ans==None : continue
    else:
        print(ans)
        break
for i in range(start,9999,1):
    ans=check_year(i)
    if ans==None:
        continue
    elif ans[0]!=ans[2] or ans[1]!=ans[3]:
        continue
    else:
        print(ans)
        break
