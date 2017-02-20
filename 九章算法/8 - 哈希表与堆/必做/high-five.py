'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        data = {}
        if not results:
            return data
        for r in results:
            if r.id not in data:
                data[r.id] = [r.score]
            else:
                data[r.id].append(r.score)
                
        for key in data:
            data[key] = sum(heapq.nlargest(5, data[key])) / 5.0
        return data