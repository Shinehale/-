cnt = 0
dots = [(i, j) for i in range(20) for j in range(21)]
lines = set()
for i in range(len(dots)):
    for j in range(i+1, len(dots)):
        if dots[j][0]-dots[i][0] != 0:
            x1, x2 = dots[i][0], dots[j][0]
            y1, y2 = dots[i][1], dots[j][1]
            k = (y2-y1)/(x2-x1)
            b = (y1*(x2-x1)-x1*(y2-y1))/(x2-x1)
            lines.add((k, b))
print(len(lines)+20)

# 40257

