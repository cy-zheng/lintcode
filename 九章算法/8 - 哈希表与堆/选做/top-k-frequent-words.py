import heapq
from functools import cmp_to_key

class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        def cmp(a, b):
            if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
                return 1
            elif a[0] == b[0] and a[1] == b[1]:
                return 0
            else:
                return -1
                
        cnt = {}
        for w in words:
            if w not in cnt:
                cnt[w] = 0
            cnt[w] += 1
        heap = []    
        for key in cnt:
            heap.append((cnt[key], key))
            
        result = heapq.nlargest(k, heap, key = cmp_to_key(cmp))
        
        return [x[1] for x in result]
            