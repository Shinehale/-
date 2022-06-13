# dp[i][j]表示状态i的情况下到达j的时候的情况数目
import math
dp=[[0]*21]*(1<<21)
mp=[[0 for i in range(21)]for j in range(21)]
for i in range(1,22):
    for j in range(1,22):
        if math.gcd(i,j)==1:
            mp[i-1][j-1]=mp[j-1][i-1]=1
for i in range(1,(1<<21)):
    if i&1:
        for k in range(21):
            if not (i >> k) & 1:
                continue
            for j in range(21):
                if ((i ^ (1 << k)) >> j) & 1 and mp[k][j]:
                    dp[i][k] += dp[i ^ (1 << k)][j]

print(dp[(1<<21)-1])
# ans=0
# for i in range(1,21):
#     if mp[i][0]:
#         ans+=dp[(1<<21)-1][i]
# print(ans)