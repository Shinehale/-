tot = 0
for k in range(1, 100):
    ans = k ** 3
    string = str(ans)
    ans = 0
    for each in string:
        ans += int(each)
    if ans == k:
        tot += 1
print(tot)
# 1A