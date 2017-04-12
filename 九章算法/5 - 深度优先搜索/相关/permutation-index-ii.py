class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return 0

        index, factor, multi_fact = 1, 1, 1
        counter = {}
        for i in xrange(len(A) - 1, -1, -1):
            if A[i] not in counter:
                    counter[A[i]] = 0
            counter[A[i]] += 1
            multi_fact *= counter[A[i]]
            rank = 0
            for j in xrange(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor / multi_fact
            factor *= (len(A) - i)

        return index