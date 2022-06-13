R=list(map(int,input().split()))
N,M=R[0],R[1]
a=[[-100000 for i in range(M)] for k in range(N)]
for i in range(N):
    R = list(map(int, input().split()))
    for j in range(M):
        a[i][j]=R[j]
dp=[[0 for i in range(M)] for k in range(N)]
dis=[(0,1),(1,0),(1,1),(1,2),(2,1),(0,2),(2,0),(0,3),(3,0)]
dp[0][0]=a[0][0]
for i in range(N):
    for j in range(M):
        for each in dis:
            x=i+each[0]
            y=j+each[1]
            if x>=N or y>=M:
                continue
            dp[x][y]=max(dp[x][y],dp[i][j]+a[x][y])
print(dp[N-1][M-1])