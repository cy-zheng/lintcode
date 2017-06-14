/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */
import java.util.*; 

public class Solution {
    /**
     * @param nodes a array of Directed graph node
     * @return a connected set of a directed graph
     */
    private int find(int[] father, int x) {
        if (father[x] == x) {
            return x;
        }
        int result = find(father, father[x]);
        father[x] = result;
        return result;
    } 
    
    private void connect(int[] father, int x, int y) {
        int xFather = find(father, x);
        int yFather = find(father, y);
        father[xFather] = yFather;
    }
    
    public List<List<Integer>> connectedSet2(ArrayList<DirectedGraphNode> nodes) {
        // Write your code here
        List<List<Integer>> result = new ArrayList<>();
        Map<Integer, List<Integer>> mapResult = new HashMap<>();
        Map<DirectedGraphNode, Integer> mapHelper = new HashMap<>();
        if (nodes == null || nodes.size() == 0) {
            return result;
        }
        int[] father = new int[nodes.size()];
        for (int i = 0; i < nodes.size(); i++){
            father[i] = i;
            mapHelper.put(nodes.get(i), i);
        }
        for (int i = 0; i < nodes.size(); i++) {
            for(int j = 0; j < nodes.get(i).neighbors.size(); j++) {
                connect(father, i, mapHelper.get(nodes.get(i).neighbors.get(j)));
            }
        }
        for (int i = 0; i < nodes.size(); i++) {
            int tmp = find(father, i);
            if (!mapResult.containsKey(tmp)) mapResult.put(tmp, new ArrayList<Integer>());
            mapResult.get(tmp).add(nodes.get(i).label);
        }
        for (Integer i : mapResult.keySet()) {
            Collections.sort(mapResult.get(i));
            result.add(mapResult.get(i));
        }
        return result;
    }
}