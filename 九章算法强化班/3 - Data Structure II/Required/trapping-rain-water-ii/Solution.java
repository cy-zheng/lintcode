import java.util.*;

class Node{
    public int x, y, val;
    public Node(int x, int y, int val){
        this.x = x;
        this.y = y;
        this.val = val;
    }
}

class NodeComparator implements Comparator<Node>{
    public int compare(Node n1, Node n2){
        return n1.val - n2.val;
    }
}

public class Solution {
    /**
     * @param heights: a matrix of integers
     * @return: an integer
     */
    public int trapRainWater(int[][] heights) {
        // write your code here
        int result = 0;
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        boolean[][] visited = new boolean[heights.length][heights[0].length];
        if (heights == null || heights.length <= 2 || heights[0].length <= 2){
            return result;
        }

        Queue<Node> pq = new PriorityQueue<>(heights.length * heights[0].length, new NodeComparator());
        for (int i = 0; i < heights.length; i++){
            if (i == 0 || i == heights.length - 1){
                for (int j = 0; j < heights[0].length; j++){
                    pq.add(new Node(i, j, heights[i][j]));
                    visited[i][j] = true;
                }
            }
            else{
                pq.add(new Node(i, 0, heights[i][0]));
                visited[i][0] = true;
                pq.add(new Node(i, heights[0].length - 1, heights[i][heights[0].length - 1]));
                visited[i][heights[0].length - 1] = true;
            }
        }

        while (pq.size() > 0){
            Node node = pq.poll();
            for (int i = 0; i < 4; i++){
                int x = node.x + dx[i];
                int y = node.y + dy[i];
                if (check(visited, x, y)){
                    if (heights[x][y] >= node.val){
                        pq.add(new Node(x, y, heights[x][y]));
                    }
                    else{
                        pq.add(new Node(x, y, node.val));
                        result += node.val - heights[x][y];
                    }
                    visited[x][y] = true;
                }
            }
        }
        return result;
    }

    private boolean check(boolean[][] visited, int x, int y){
        if (x < 0 || x >= visited.length) return false;
        if (y < 0 || y >= visited[0].length) return false;
        return !visited[x][y];
    }
};