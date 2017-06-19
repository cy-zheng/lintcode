public class Solution {
    /**
     * @param heights: an array of integers
     * @return: a integer
     */
    public int trapRainWater(int[] heights) {
        // write your code here
        int index = -1;
        int max = 0;
        int result = 0;
        if (heights == null || heights.length <= 2) return result;
        for (int i = 0; i < heights.length; i++){
            if (heights[i] > max){
                max = heights[i];
                index = i;
            }
        }
        if (index == -1) return result;
        result += queueFind(heights, 0, index, true);
        result += queueFind(heights, index, heights.length - 1, false);
        return result;
    }

    private int queueFind(int[] heights, int i, int j, boolean flag){
        int result = 0;
        if (i >= j) return result;
        Queue<Integer> queue = new LinkedList<>();
        if (flag){
            for (int m = i; m <= j; m++){
                if (queue.size() > 0 && queue.peek() <= heights[m]){
                    int tmp = queue.peek();
                    while(queue.size() > 0){
                        result += tmp - queue.poll();
                    }
                }
                queue.add(heights[m]);
            }
        }
        else{
            for (int m = j; m >= i; m--){
                if (queue.size() > 0 && queue.peek() <= heights[m]){
                    int tmp = queue.peek();
                    while(queue.size() > 0){
                        result += tmp - queue.poll();
                    }
                }
                queue.add(heights[m]);
            }
        }

        return result;
    }
}