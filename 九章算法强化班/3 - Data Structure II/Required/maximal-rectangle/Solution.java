public class Solution {
    /**
     * @param matrix a boolean 2D matrix
     * @return an integer
     */
    public int maximalRectangle(boolean[][] matrix) {
        // Write your code here
        // http://blog.csdn.net/linhuanmars/article/details/24444491
        int result = 0;
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return result;
        }
        int[][] dp = new int[2][matrix[0].length];
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                if (matrix[i][j]){
                    dp[i % 2][j] = 1 + dp[(i + 1) % 2][j];
                }
                else {
                    dp[i % 2][j] = 0;
                }
            }
            result = Math.max(result, findRectangle(dp[i % 2]));
        }
        return result;
    }
    
    private int findRectangle(int[] height){
        int result = 0;
        if (height == null || height.length == 0) return result;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < height.length; i++){
            while (stack.size() > 0 && height[stack.peek()] >= height[i]){
                int index = stack.pop();
                int curArea = stack.size() > 0 ? height[index] * (i - stack.peek() - 1) 
                    : height[index] * i;
                result = Math.max(result, curArea);
            }
            stack.push(i);
        }
        while (stack.size() > 0){
            int index = stack.pop();
            int curArea = stack.size() > 0 ? height[index] * (height.length - stack.peek() - 1) 
                : height[index] * height.length;
            result = Math.max(result, curArea);
        }
        return result;
    }
}