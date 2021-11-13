from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # n = len(triangle)
        # f = [[0] * n for _ in range(n)]
        # f[0][0] = triangle[0][0]

        # for i in range(1, n):
        #     f[i][0] = f[i - 1][0] + triangle[i][0]
        #     for j in range(1, i):
        #         f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        #     f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        
        # return min(f[n - 1])
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]
        for i in range(1, n):
            # 每一行最后一列只能从上一行的最后一列到达
            f[i] = f[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                f[i] = min(f[j], f[j-1]) + triangle[i][j]
            # 每一行的开始只能从上一行的第一列到达
            f[0] += triangle[i][0]
        return min(f)

if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    solution = Solution()
    res = solution.minimumTotal(triangle=triangle)
    print(res)