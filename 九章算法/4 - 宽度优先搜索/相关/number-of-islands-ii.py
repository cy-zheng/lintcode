# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        point2label = [[0 for i in xrange(m)] for j in xrange(n)]
        label2point = {}
        result = [0]
        move_x = [1, -1, 0, 0, 0]
        move_y = [0, 0, 1, -1, 0]
        label_count = 1
        for operator in operators:
            flag = True
            neighbors_label = set([])
            for i in range(len(move_x)):
                if self.test_point(point2label, operator.x + move_x[i],
                   operator.y + move_y[i], n, m):
                    flag = False
                    neighbors_label.add(
                            point2label[operator.x + move_x[i]][operator.y + move_y[i]]
                        )
            neighbors_label = list(neighbors_label)
            if flag:
                point2label[operator.x][operator.y] = label_count
                label2point[label_count] = [(operator.x, operator.y)]
                label_count += 1
                result.append(result[-1] + 1)
            else:
                final_label = neighbors_label.pop(0)
                for label in neighbors_label:
                    for point in label2point[label]:
                        point2label[point[0]][point[1]] = final_label
                    label2point[final_label].extend(label2point[label])
                    del label2point[label]

                point2label[operator.x][operator.y] = final_label
                label2point[final_label].append((operator.x, operator.y))
                result.append(result[-1] - len(neighbors_label))
                    
        return result[1:]
        
    def test_point(self, cache, x, y, n, m):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if cache[x][y] != 0:
            return True
        return False