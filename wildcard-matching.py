"""
f[i][j]表示s的前i个字符和p的前j个字符是否能匹配

1. p[j] == ?  f[i][j] <- f[i-1][j-1]  
2. p[j] == *  f[i][j] <- f[i-1][j] or f[i][j-1]
3. p[j] == s[i]   f[i][j] <- f[i-1][j-1]
""" 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        
        s = " " + s
        p = " " + p
        
        for i in range(1, n+1):
            if p[i] == "*":
                f[0][i] = True
            else:
                break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j] == "*":
                    f[i][j] = f[i][j-1] or f[i-1][j]
                elif p[j] == "?" or s[i] == p[j]:
                    f[i][j] = f[i-1][j-1]

        return f[m][n]
