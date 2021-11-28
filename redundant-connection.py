class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.n = 0
        for edge in edges:
            x = edge[0]
            y = edge[1]
            self.n = max(self.n, max(x, y))
        self.fa = [i for i in range(self.n + 1)]
        for edge in edges:
            x = edge[0]
            y = edge[1]
            nx = self.find(x)
            ny = self.find(y)
            if nx == ny:
                return edge
            else:
                self.unionSet(nx, ny)

    def find(self, x):
        if x == self.fa[x]:return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def unionSet(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
    #     self.n = 0
    #     for l in edges:
    #         x = l[0]
    #         y = l[1]
    #         self.n = max(self.n, max(x, y))
    #     self.to = list()
    #     for i in range(self.n + 1):
    #         self.to.append(list())
    #     for l in edges:
    #         x = l[0]
    #         y = l[1]
    #         # 出边数组加边
    #         self.to[x].append(y)
    #         self.to[y].append(x)
    #         self.hascycle = 0
    #         self.visited = [0 for _ in range(self.n + 1)]
    #         self.dfs(x, 0)
    #         if self.hascycle == 1:  
    #             return l
    #     return list()

    # def dfs(self, x, fa):
    #     self.visited[x] = 1
    #     for y in self.to[x]:
    #         if y == fa: 
    #             continue
    #         if not self.visited[y]:
    #             self.dfs(y, x)
    #         else: 
    #             self.hascycle = 1
