import sys
import os

dt={}
for i in range(10):
    dt[i]=0

for i in range(2021):
    s=str(i)
    for x in s:
        dt[int(x)]+=1
print(dt[2])