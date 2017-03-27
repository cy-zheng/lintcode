import heapq

class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        # Write your code here
        index = [0 for i in range(len(arrays))]
        heap = []
        result = []
        for i in range(len(arrays)):
            if index[i] < len(arrays[i]):
                heap.append((arrays[i][index[i]], i))
                index[i] += 1
        heapq.heapify(heap)
        while heap:
            temp = heapq.heappop(heap)
            result.append(temp[0])
            if index[temp[1]] < len(arrays[temp[1]]):
                heapq.heappush(heap, (arrays[temp[1]][index[temp[1]]], temp[1]))
                index[temp[1]] += 1
        return result