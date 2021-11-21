class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:return 1
        squares = list()
        for i in range(1, n):
            if i * i <= n:
                squares.append(i * i)
            else:
                break
        m = len(squares)
        squares.insert(0, 0)
        #f[i][j]表示用前i完全平方数的和表示j的最小数量
        #                 前i-1个完全平方数可以表示j了     前i-1个完全平方数能表示j-square[i]
        # f[i][j] = min(f[i-1][j], f[i-1][j-square[i]])
        f = [1e9] * (n+1)
        f[0] = 0
        for i in range(1, m+1):
            for j in range(squares[i], n+1):
                f[j] = min(f[j], f[j-squares[i]] + 1)

        return f[n]
