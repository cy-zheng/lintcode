# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import heapq
from functools import cmp_to_key

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        if not points or not origin or k is None:
            return []
            
        def cmp(p1, p2):
            dis_1 = (p1.x - origin.x) ** 2 + (p1.y - origin.y) ** 2
            dis_2 = (p2.x - origin.x) ** 2 + (p2.y - origin.y) ** 2
            if dis_1 < dis_2:
                return -1
            elif dis_1 > dis_2:
                return 1
            else:
                if p1.x < p2.x:
                    return 1
                elif p1.x > p2.x:
                    return -1
                elif p1.y < p2.y:
                    return 1
                elif p1.y > p2.y:
                    return -1
                return 0
        
        key = cmp_to_key(cmp)        
        return heapq.nsmallest(k, points, key)