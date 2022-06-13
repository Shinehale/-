R = list(map(int, input().split()))
m, n = R[0], R[1]
width = (R[1] // 2) * 2 + R[0]
pos1, pos2 = 0, width - m
for i in range(n):
    for j in range(width):
        if ((j - pos1) < m and j - pos1 >= 0) or ((j - pos2) < m and j - pos2 >= 0):
            print("*", end="")
        else:
            print(".", end="")
    print("")
    pos1 += 1
    pos2 -= 1
# 1A