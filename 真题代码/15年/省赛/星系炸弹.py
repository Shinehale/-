tot14=30-9+31
tot15=365
tot16=366
tot17=1000-tot14-tot15-tot16
s=[31,28,31,30,31,30,31,31,30,31,30,31]
pos=0
for i in range(len(s)):
    if tot17>s[i]:
        tot17-=s[i]
    else:
        pos=i+1
        break
print("2017-%02d-%02d" %(pos,tot17))