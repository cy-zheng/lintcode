class Solution:
    # @param {int[]} org a permutation of the integers from 1 to n
    # @param {int[][]} seqs a list of sequences
    # @return {boolean} true if it can be reconstructed only one or false
    def sequenceReconstruction(self, org, seqs):
        # Write your code here
        from collections import defaultdict
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
            for i in xrange(len(seq)):
                if i == 0:
                    indegrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1

        cur = [k for k in indegrees if indegrees[k] == 0]
        res = []

        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in edges[cur_node]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org