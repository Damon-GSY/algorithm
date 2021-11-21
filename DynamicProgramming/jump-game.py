class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # move nums to 1-based
        nums.insert(0, 0)
        # f[i][j]表示前i个数字能否到第j个位置
        # f[i][j] = f[i-1][j] or f[i-1][j-nums[j]]

        f = [[0 for i in range(n + 1)] for i in range(n + 1)]

        for i in range(1, n+1):
            f[i][1] = 1

        print(f) 
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if 0 < j - nums[j] <= n: 
                    f[i][j] = f[i-1][j] or f[i-1][j-nums[j]]
                else:
                    f[i][j] = f[i-1][j]

        print(f)
        return f[n][n]
