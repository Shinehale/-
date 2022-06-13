"""
我们有如下定义：
dp[i][j]表示为放到第i个骰子，最上面是j的情况下，已经有的方案数
那么不难定义：
dp[i][j]=sum(dp[i-1][k]) 其中k是可以跟j相容的面
那么当n达到1e9的情况时，我们不难判断出来需要矩阵快速幂来实现这样快速计算
"""

Mod = 10 ** 9 + 7


class Matrix:
    def __init__(self, n, m, mod):
        self.a = [[0 for i in range(m)] for j in range(n)]
        self.Mod = mod
        self.n = n
        self.m = m

    def __mul__(self, other):
        ans = Matrix(self.n, other.m, other.Mod)
        for i in range(self.n):
            for j in range(other.m):
                ans.a[i][j]=0
                for k in range(self.m):
                    ans.a[i][j] += self.a[i][k] * other.a[k][j]%Mod
                    ans.a[i][j] %= self.Mod
        return ans

    def set_value(self, lis):
        for i in range(self.n):
            for j in range(self.m):
                self.a[i][j] = lis[i][j]

    def out_print(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end=" ")
            print("")


def calc(Tar, times):
    Base = Tar
    times -= 1
    while times>0:
        if times & 1:
            Base = Base * Tar
            Tar = Tar * Tar
            times >>= 1
    return Base


reverse = [0, 4, 5, 6, 1, 2, 3]
R = list(map(int, input().split()))
N, M = R[0], R[1]
mp = [[4 for i in range(6)] for j in range(6)]
for i in range(M):
    R = list(map(int, input().split()))
    posx1, posy1 = R[0] - 1, reverse[R[1]] - 1
    posx2, posy2 = reverse[R[0]] - 1, R[1] - 1
    mp[posx1][posy1] = 0
    mp[posx2][posy2] = 0
Ma = Matrix(6, 6, Mod)
Ma.set_value(mp)
print(mp)
Back = calc(Ma, N - 1)
ans = 0
BaseMatrix = Matrix(6, 1, Mod)
BaseMatrix.set_value([[4] for i in range(6)])
Back = Back * BaseMatrix
for i in range(6):
    ans += Back.a[i][0]%Mod
    ans = ans % Mod
print(ans)
"""
import math
mod = int(math.pow(10,9))+7
def multi(A, B):    #矩阵乘法
    C = [[0]*6 for i in range(6)]
    for i in range(6):
      for j in range(6):
         for k in range(6):
            C[i][j] = int((C[i][j] + A[i][k] * B[k][j]) % mod)
    return C

def power(A, n):    #矩阵快速幂
    res = [[0]*6 for i in range(6)]
    for i in range(6):
        res[i][i] = 1
    while n:
        if n % 2:
            res = multi(res, A)
        A = multi(A, A)
        n >>= 1
    return res

def solve(n, dice):
    transfer = [[4]*6 for i in range(6)]  #转移矩阵
    for i in range(6):                  #去掉互斥的情况
        for j in dice.get((i+3)%6,[]):  #0对面是3，1对4，2对5
            transfer[i][j]= 0
    transfer = power(transfer, n-1)     #转移矩阵乘n-1次
    temp = [4]*6                        #表示最下面的骰子
    ans = [0]*6
    for i in range(6):                  #最后乘最下面的骰子
        for j in range(6):
            ans[i] += transfer[i][j] * temp[j]
    print(int(sum(ans) % mod))

n, m = [int(str) for str in input().split()]
dice = dict()                  #用字典记录互相排斥的面
for i in range(m):
   x, y = [int(str)-1 for str in input().split()]
   if x not in dice:   dice[x] = [y]
   else:               dice[x].append(y)
   if y not in dice:   dice[y] = [x]
   else:               dice[y].append(x)
solve(n, dice)



"""

"""
2 3 
4 1 
6 6 
2 4
"""