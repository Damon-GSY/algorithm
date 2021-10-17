class NumMatrix:
    # sum[i][j] = sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+nums[i][j]

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        # [[0 for i in range(m)] for j in range(n)]
        presum = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1]-presum[i-1][j-1] + matrix[i-1][j-1]
        self.presum = presum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        row2+=1
        col1+=1
        col2+=1
        presum = self.presum
        return presum[row2][col2]- presum[row2][col1-1]-presum[row1-1][col2]+presum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
