class Solution:
    # @param {string} s a string
    # @param {set[str]} wordDict a set of words
    def __init__(self):
        self.cache = {}
        self.dict = {}
        self.dp_cache = []
        
    def wordBreak(self, s, wordDict):
        # Write your code here
        result = []
        if not s:
            return result
        self.dp_cache = [False for i in range(len(s) + 1)]
        self.dp_cache[-1] = True
        for w in wordDict:
            self.dict[w] = True
        self.dp(s, wordDict)
        candidates = range(1, len(s))
        self.dfs(candidates, 0, [], result, s)
        for i in range(len(result)):
            result[i] = ' '.join(result[i])
        return result
        
    def dp(self, s, wordDict):
        for i in range(len(s))[::-1]:
            for j in range(i + 1, len(s) + 1):
                self.dp_cache[i] = self.dp_cache[i] or \
                        (self.dp_cache[j] and (self.dict.get(s[i:j], False)))
        
    def dfs(self, candidates, start_num, subset, result, s):
        temp = [0] + subset + [len(s)]
        if self.testPalindrome(s, temp[-2], len(s)):
            result_temp = []
            for i in range(len(temp) - 1):
                result_temp.append(s[temp[i]:temp[i + 1]])
            result.append(result_temp)
        for i in range(start_num, len(candidates)):
            subset.append(candidates[i])
            if self.dp_cache[candidates[i]] and self.testPalindrome(s, 
                                   0 if len(subset) == 1 else subset[-2], 
                                   subset[-1]):
                #剪枝，如果加入的index不在dict中，那么就不需要这个分支了
                self.dfs(candidates, i + 1, subset, result, s)
            subset.pop()
        
    def testPalindrome(self, s, i, j):
        #做个cache，省的一次一次判断
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        result = self.dict.get(s[i:j], False)
        self.cache[(i, j)] = result
        return result