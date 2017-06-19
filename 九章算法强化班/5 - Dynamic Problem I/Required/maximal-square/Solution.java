public class Solution {
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        // write your code here
        int result = 0;
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }
        int[][] dp = new int[2][matrix[0].length + 1];
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                if (matrix[i][j] == 1){
                    dp[i % 2][j + 1] = Math.min(dp[(i + 1) % 2][j + 1],
                            Math.min(dp[(i + 1) % 2][j], dp[i % 2][j])) + 1;
                    result = Math.max(result, dp[i % 2][j + 1]);
                }
                else{
                    dp[i % 2][j + 1] = 0;  // it's important!
                }
            }
        }
        return result * result;
    }
}