def dfs(i, j, step):
    global count, flag
    if step > 16:
        return
    if step == 16:
        count += 1
        return
    for k in range(4):
        i2 = i + d[k][0]
        j2 = j + d[k][1]
        if i2 >= 0 and i2 <= 3 and j2 >= 0 and j2 <= 3 and flag[i2][j2] == False:
            flag[i2][j2] = True
            dfs(i2, j2, step + 1)
            flag[i2][j2] = False


count = 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(4):
    for j in range(4):
        flag = [[False for _ in range(4)] for _ in range(4)]
        flag[i][j] = True
        dfs(i, j, 1)
print(count)
