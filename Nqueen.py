class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.used = [0 for _ in range(n)]
        self.usedPlus = set()
        self.usedMinus = set()
        self.p = list()
        self.ans = list()
        self.dfs(0)
        self.res = list()
        for a in range(len(self.ans)):
            self.res.append(list())
            ans = self.ans[a]
            for index in ans:
                temp = ''
                for i in range(n):
                    if i == index:
                        temp += 'Q'
                    else:
                        temp += '.'
                self.res[a].append(temp)
        return self.res
 
    
    def dfs(self, row: int):
        if row == self.n:
            self.ans.append(self.p[:])
            return
        for col in range(self.n):
            if not self.used[col] and row + col not in self.usedPlus and row - col not in self.usedMinus:
                self.p.append(col)
                self.used[col] = 1
                self.usedPlus.add(row + col)
                self.usedMinus.add(row - col)
                self.dfs(row + 1)
                self.used[col] = 0
                self.usedPlus.remove(row + col)
                self.usedMinus.remove(row - col)
                self.p.pop()
