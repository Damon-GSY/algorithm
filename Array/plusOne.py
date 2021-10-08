class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 倒序遍历
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            #第一次是最后一位进位
            digits[i] %= 10
            #如果倒数第二位之后有数字不需要进位，则返回列表
            if digits[i] != 0:
                return digits
        #说明全部数字都进位，这需要在最大位置插入1
        digits.insert(0, 1)
        return digits