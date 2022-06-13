import os
import sys

def calc():
    R=input().split()
    n = int(R[0])
    sum1=0
    sum2=0
    for i in range(n):
        value=int(input())
        if value>=85 : sum1+=1
        if value>=60 : sum2+=1
    ans1=float(sum1)/n*100
    ans2=float(sum2)/n*100
    print("{}%".format(int(ans2+0.5)))
    print("{}%".format(int(ans1+0.5)))

calc()