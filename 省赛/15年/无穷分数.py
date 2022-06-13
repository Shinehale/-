ans=1
for k in range(100000,0,-1):
    ans=k/(ans+k)
print("%.5f" %ans)
# 1A