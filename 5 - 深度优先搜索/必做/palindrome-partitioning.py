class Solution:
    # @param s, a string
    # @return a list of lists of string
    def __init__(self):
        self.cache = {}
  
    def partition(self, s):
        # write your code here
        result = []
        if not s:
            result.append([])
            return result
        candidates = range(1, len(s))
        self.dfs(candidates, 0, [], result, s)
        return result
        
    def dfs(self, candidates, start_num, subset, result, s):
        temp = [0] + subset + [len(s)]
        result_temp = []
        isPalindrome = True
        for i in range(len(temp) - 1):
            if self.testPalindrome(s, temp[i], temp[i + 1]):
                result_temp.append(s[temp[i]:temp[i + 1]])
            else:
                isPalindrome = False
                break
        if isPalindrome:
            result.append(result_temp)
        for i in range(start_num, len(candidates)):
            subset.append(candidates[i])
            if self.testPalindrome(s, 
                                   0 if len(subset) == 1 else subset[-2], 
                                   subset[-1]):
                #剪枝，如果加入的index破坏了回文，那么就不需要这个分支了
                self.dfs(candidates, i + 1, subset, result, s)
            subset.pop()
        
    def testPalindrome(self, s, i, j):
        #做个cache，省的一次一次判断
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        result = s[i:j] == s[i:j][::-1]
        self.cache[(i, j)] = result
        return result

            
        
                