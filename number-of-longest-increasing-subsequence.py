class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        cnt = [0] * n
        max_len = 0
        ans = 0
        # f[0] = 1
        # f[i]表示以第nums[i]结尾的最长递增子序列的长度
        # cnt[i]表示以nums[i]结尾的最长递增子序列的个数
        for i, x in enumerate(nums):
            f[i] = 1
            cnt[i] = 1
            for j in range(i):
                if nums[j] < x:
                    # f[i] = max(f[j]+1, f[i]) <-> f[i] = max(f[j]) 1 <=j < n
                    if f[j] + 1 > f[i]:
                        f[i] = f[j] + 1
                        # 之前j对应的所有最长递增子序列的个数 和 i对应的个数应该相同
                        # j : [1, 2, 3], [-1, 2, 3], [-9, 2, 3]
                        # i : [1, 2, 3, 10], [-1, 2, 3, 10], [-9, 2 ,3, 10]
                        cnt[i] = cnt[j]
                    elif f[j] + 1 == f[i]:
                        # 说明以j结尾的最长递增子序列的长度 加上nums[i]之后， 新的长度和本身以nums[i]结尾的最长子序列的长度是一样
                        cnt[i] += cnt[j]
        
        max_len = max(f)
        for i in range(n):
            if f[i] == max_len:
                ans += cnt[i]
        return ans
