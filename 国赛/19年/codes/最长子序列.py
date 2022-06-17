S = input().strip()
T = input().strip()

j = 0
for i in range(len(S)):
    if S[i] == T[j]:
        j = j + 1
print(j)