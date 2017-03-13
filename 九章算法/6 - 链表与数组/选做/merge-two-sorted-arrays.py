class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        result = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        if i < len(A):
            result.extend(A[i:])
        elif j < len(B):
            result.extend(B[j:])
        return result
        