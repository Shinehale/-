import os
import sys

N,M=map(int,input().split())
for i in range(N+1):
    if i==0:
        for j in range(M+1):
            if j==0:
                print("┌",end="")
            elif j==M:
                print("─┐")
            else:
                print("─┬",end="")
    elif i==N:
        for j in range(M+1):
            if j==0:
                print("│",end="")
            else:
                print(" │",end="")
        print("")
        for j in range(M+1):
            if j==0:
                print("└",end="")
            elif j==M:
                print("─┘")
            else:
                print("─┴",end="")
    else:
        for j in range(M+1):
            if j==0:
                print("│",end="")
            else:
                print(" │",end="")
        print("")
        for j in range(M+1):
            if j==0:
                print("├",end="")
            elif j==M:
                print("─┤")
            else:
                print("─┼",end="")
