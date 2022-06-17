def primeResolve(n):
    ans = []
    if n < 2:
        return 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                ans.append(i)
                n = n // i
        elif n < i:
            break
    if n > 1:
        ans.append(n)
    return ans


dp = [0] * 100
for i in range(2, 101):
    for j in primeResolve(i):
        dp[j] += 1
ans = 1
for k in dp:
    if k != 0:
        ans *= (k + 1)
print(ans)
