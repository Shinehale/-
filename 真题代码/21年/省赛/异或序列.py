"""
 可以证明异或顺序对异或结果不造成影响，说明满足异或满足交换律
 如果有平局的情况则A^B=0，那么所有结果异或都是零
 这里要求比较最终结果大小，显然考虑的是最高位的数字
"""
T = int(input())
for times in range(T):
    R = list(map(int, input().split()))
    N, mx, tot = R[0], 0, 0
    Lis = []
    for i in range(1, N + 1):
        mx = max(mx, R[i])
        tot = tot ^ R[i]
        Lis.append(R[i])
    if tot == 0:
        print(0)
        continue
    x = 1
    while x < mx:
        x <<= 1
    while x:
        sum_one, sum_zero = 0, 0
        for each in Lis:
            if each & x == 0:
                sum_zero += 1
            else:
                sum_one += 1
        if sum_one % 2 == 1:
            if sum_zero % 2 == 1 and sum_one > 1:
                print(-1)
            else:
                print(1)
            break
        x >>= 1
"""
如果最高位1的个数是偶数，那么这位无影响，只需要考虑下一位即可
如果这位1的个数是奇数，那么分成两种情况
    1.如果这一位的0的个数为偶数，那么后手肯定能控制最后一个0，则后手赢
    2.如果这一位的0的个数为奇数，那么无论怎样，先手一定赢
"""