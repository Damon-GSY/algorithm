class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 首先构造presum，然后再利用哈希表（presum, count)去检查是否存在i, j 使得 pre[i]-pre[j] == k
        presum = dict()
        pre = 0
        presum[0] = 1
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in presum.keys():
                count += presum[pre-k]
            if pre not in presum.keys():
                presum[pre] = 1
            else:
                presum[pre] += 1
        return count
