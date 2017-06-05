import java.util.*;

class Pair{
    public int x, y, val;
    public Pair(int x, int y, int val){
        this.x = x;
        this.y = y;
        this.val = val;
    }
}

class PairComparator implements Comparator<Pair>{
    public int compare(Pair a, Pair b){
        return a.val - b.val;
    }
}


public class Solution {
    /**
     * @param A an integer arrays sorted in ascending order
     * @param B an integer arrays sorted in ascending order
     * @param k an integer
     * @return an integer
     */
    public int kthSmallestSum(int[] A, int[] B, int k) {
        // Write your code here
        int[] dx = {0, 1};
        int[] dy = {1, 0};
        int m = A.length;
        int n = B.length;
        boolean[][] visited = new boolean[m][n];
        PriorityQueue<Pair> pq = new PriorityQueue<>(k, new PairComparator());
        pq.add(new Pair(0, 0, A[0] + B[0]));
        for (int i = 0; i < k - 1; i++){
            Pair cur = pq.poll();
            for(int j = 0; j < 2; j++){
                int x = cur.x + dx[j];
                int y = cur.y + dy[j];
                if (x < m && y < n && !visited[x][y]){
                    visited[x][y] = true;
                    pq.add(new Pair(x, y, A[x] + B[y]));
                }
            }
        }
        return pq.peek().val;
    }
}