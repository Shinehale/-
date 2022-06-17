n = int(input().strip())
S = 0
for i in range(1, n):
    S = (S + i * (n - i) * (n - i)) % (10 ** 9 + 7)

print(S)