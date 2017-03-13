class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                i += 1
            else:
                A.insert(i, B[j])
                A.pop()
                m += 1
                i += 1
                j += 1
        while j < n:
            A[i] = B[j]
            i += 1
            j += 1
        return A
        