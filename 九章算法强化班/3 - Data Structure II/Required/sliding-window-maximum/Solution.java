import java.util.*;

public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    public ArrayList<Integer> maxSlidingWindow(int[] nums, int k) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (nums == null || nums.length < k) return result;
        Queue<Integer> pq = new PriorityQueue<Integer>();
        for (int i = 0; i < nums.length; i++){
            pq.add(-nums[i]);
            if (i >= k){
                pq.remove(-nums[i - k]);
            }
            if (i >= k - 1){
                result.add(-pq.peek());
            }
        }
        return result;
    }
}
