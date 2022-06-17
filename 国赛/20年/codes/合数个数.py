sum = 0
for i in range(3, 2021):
    for j in range(2, i):
        if i % j == 0:
            sum += 1
            break
print(sum)
