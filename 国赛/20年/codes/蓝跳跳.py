p, b, s = map(int, input().split())
dp = [[0 for i1 in range(2)] for i in range(s + 1)]
dp[0][1] = 1
dp[1][0] = 1
for i in range(2, s + 1):
    for j in range(1, b):
        if i - j < 0:
            break
        dp[i][0] += ((dp[i - j][1] + dp[i - j][0]) % 20201114)

    for j in range(b, p + 1):
        if i - j < 0:
            break
        dp[i][1] += dp[i - j][0] % 20201114

print(sum(dp[s]) % 20201114)


