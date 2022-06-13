s1=input()
n=len(s1)
s2="".join(reversed(list(s1)))
dp=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(n-dp[n][n])