class Solution:
    def __init__(self):
        # 每一次递归的共享变量
        self.a = list()
        # 数组长度
        self.n = 0
        # 布尔数组判断数字是否被选择
        self.chosen = list()
        self.ans = list()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        # 构建布尔数组
        for i in range(0, self.n):
            self.chosen.append(0)
        self.recur(nums, 0)
        return self.ans

    def recur(self, nums:List[int], pos:int):
        # 递归边界
        if pos == self.n:
            # 去重
            if self.a not in self.ans:
                self.ans.append(self.a[:])
            return
        
        for i in range(0, self.n):
            if not self.chosen[i]:
                self.a.append(nums[i])
                self.chosen[i] = 1
                self.recur(nums, pos+1)
                # 还原现场
                self.chosen[i] = 0
                self.a.pop()
            
