class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        n = len(grid)
        m = len(grid[0])
        self.fa = [i for i in range(m * n + 1)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":continue
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if grid[nx][ny] == "1":
                        self.unionSet(self.nums(i, j), self.nums(nx, ny))

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and self.find(self.nums(i, j)) == self.nums(i, j):
                    ans += 1

        return ans

    def unionSet(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
    
    def find(self, x):
        if x == self.fa[x]:return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def nums(self, i , j):
        return i * self.m + j
