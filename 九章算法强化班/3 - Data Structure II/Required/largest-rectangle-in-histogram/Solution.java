import java.util.*;

public class Solution {
    /**
     * @param height: A list of integer
     * @return: The area of largest rectangle in the histogram
     */
    public int largestRectangleArea(int[] height) {
        // write your code here
        // http://blog.csdn.net/linhuanmars/article/details/20524507
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
