import heapq

class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element
    def kthLargestElement2(self, nums, k):
        # Write your code here
        # 本题重点：N is much larger than k
        # 不能使用O(n)的quick select，而要使用O(klogn)的堆排序
        return heapq.nlargest(k, nums)[-1]