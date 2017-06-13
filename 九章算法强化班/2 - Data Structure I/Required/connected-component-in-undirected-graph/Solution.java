/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
import java.util.*;

public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        // Write your code here
        List<List<Integer>> result = new ArrayList<>();
        if (nodes == null || nodes.size() == 0) return result;

        Set<UndirectedGraphNode> unvisited = new HashSet<UndirectedGraphNode>();
        for(UndirectedGraphNode node : nodes) unvisited.add(node);
        Queue<UndirectedGraphNode> queue = new ArrayDeque<>();

        while(unvisited.size() > 0){
            Iterator<UndirectedGraphNode> it = unvisited.iterator();
            queue.add(it.next());
            it.remove();
            List<Integer> tmp = new ArrayList<>();
            while (queue.size() > 0){
                UndirectedGraphNode cur = queue.poll();
                tmp.add(cur.label);
                for (UndirectedGraphNode next : cur.neighbors){
                    if (unvisited.contains(next)){
                        unvisited.remove(next);
                        queue.add(next);
                    }
                }
            }
            result.add(tmp);
        }

        for(int i = 0; i < result.size(); i++){
            Collections.sort(result.get(i));
        }

        return result;
    }
}