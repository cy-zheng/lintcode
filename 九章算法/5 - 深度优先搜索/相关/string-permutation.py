class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        dictA = {}
        dictB = {}
        for word in A:
            dictA.setdefault(word, 0)
            dictA[word] += 1
            
        for word in B:
            dictB.setdefault(word, 0)
            dictB[word] += 1
            
        return dictA == dictB
