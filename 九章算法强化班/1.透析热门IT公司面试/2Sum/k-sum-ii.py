class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        result = []
        if not A:
            return result
        self.dfs(A, 0, [], k, target, result)
        return result
        
    def dfs(self, A, index, sublist, k, target, result):
        if len(sublist) == k:
            if sum(sublist) == target:
                result.append(sublist[:])
            return
        for i in range(index, len(A)):
            sublist.append(A[i])
            self.dfs(A, i + 1, sublist, k, target, result)
            sublist.pop()