public class Solution {
    /**
     * @param A an integer matrix
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequenceII(int[][] A) {
        // Write your code here
        int result = 0;
        if (A == null || A.length == 0) return result;
        int[][] dp = new int[A.length][A[0].length];
        boolean[][] flag = new boolean[A.length][A[0].length];
        
        for (int i = 0; i < A.length; i++){
            for (int j = 0; j < A[0].length; j++){
                result = Math.max(result, search(A, dp, flag, i, j));
            }
        }
        return result;
    }
    
    private int search(int[][] A, int[][] dp, boolean[][] flag, int i, int j){
        if (flag[i][j]) return dp[i][j];
        
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        int result = 1;
        for (int k = 0; k < 4; k++){
            int x = i + dx[k];
            int y = j + dy[k];
            if (valid(A, x, y) && A[x][y] > A[i][j]){
                result = Math.max(result, search(A, dp, flag, x, y) + 1);
            }
        }
        flag[i][j] = true;
        dp[i][j] = result;
        return result;
    }
    
    private boolean valid(int[][] A, int x, int y){
        if (x < 0 || x >= A.length) return false;
        if (y < 0 || y >= A[0].length) return false;
        return true;
    }
}