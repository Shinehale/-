def calc(pos):
    pos = pos - 1
    line = pos // (w * 2)
    new_pos = pos % (2 * w)
    new_pos += 1
    if new_pos <= w:
        col = new_pos
        line = line * 2 + 1
    else:
        col = 2 * w - new_pos + 1
        line = line * 2 + 2
    return (line, col)


R = list(map(int, input().split()))
w, m, n = R[0], R[1], R[2]
fir, sec = calc(m), calc(n)
ans = abs(fir[0] - sec[0]) + abs(fir[1] - sec[1])
print(ans)
# 1A