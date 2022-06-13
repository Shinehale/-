N=int(input())
ans=N
while N>=3:
    new_=N//3
    ans+=new_
    N=N%3+new_
print(ans)
# 1A