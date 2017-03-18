class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        result = 1
        factor = 1
        for i in xrange(len(A)-1, -1, -1):
            # rank是在A[i]后比A[i]小的数字个数
            rank = 0
            for j in xrange(i+1, len(A)):
                if A[i] > A[j]:
                    rank +=1
            # factor是位数的影响，越高位影响越大
            result += factor*rank
            factor *= len(A)-i
        return result