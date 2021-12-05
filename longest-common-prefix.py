class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]

        prefix = strs[0]
        for i in range(1, n):
            s = strs[i]
            prefix = self.findLcs(prefix, s)
            if prefix == "":
                return ""
        
        return prefix

    def findLcs(self, x, y):
        n = len(x)
        m = len(y)
        res = ""
        for i in range(min(n, m)):
            if x[i] == y[i]:
                res += x[i]
            else:
                break
        return res
