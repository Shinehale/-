n = int(input())
lists = list(map(int, input().split()))
count = 0
for i in range(n):
    if lists[i] == i + 1:
        continue
    else:
        index = lists.index(i+1)
        lists[i],lists[index] = lists[index],lists[i]
        count += 1
print(count)