class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 下界
        left = max(weights)
        # 上界
        right = sum(weights)
        while(left < right):
            needDay = 1
            # 计算当前能承载的重量
            curWeights = 0
            mid = (left + right) // 2
            for weight in weights:
                # 比较当前的货物是否还能上船
                if curWeights + weight > mid:
                    needDay += 1
                    curWeights = 0
                curWeights += weight
            if needDay <= days:
                right = mid
            else:
                left = mid + 1
        return right
