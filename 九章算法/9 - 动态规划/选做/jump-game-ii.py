class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if not A:
            return -1
            
        max_step = A[0]
        count = 1
        max_next = A[0]
        for index, num in enumerate(A):
            if index > max_step:
                max_step = max_next
                count += 1
            max_next = max(max_next, index + num)
            
        return count
            