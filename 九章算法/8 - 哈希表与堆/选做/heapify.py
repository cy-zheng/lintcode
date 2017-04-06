class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        if not A:
            return A
        for i in xrange(len(A)):
            index = i
            while index != 0 and A[index] < A[(index - 1) / 2]:
                A[index], A[(index - 1) / 2] = A[(index - 1) / 2], A[index]
                index = (index - 1) / 2
        return A