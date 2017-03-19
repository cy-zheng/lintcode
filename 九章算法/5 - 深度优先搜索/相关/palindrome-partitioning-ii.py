class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        n = len(s)
        f = []
        # 后一个字符串可以由p[i + 1][j - 1] and s[i] == s[j]判断出来
        p = [[False for x in range(n)] for x in range(n)]
        #the worst case is cutting by each char
        for i in range(n+1):
            f.append(n - 1 - i) # the last one, f[n]=-1
        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]