import java.util.*;

public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: the median of numbers
     */
    public int[] medianII(int[] nums) {
        // write your code here
        Queue<Integer> left = new PriorityQueue<>();
        Queue<Integer> right = new PriorityQueue<>();
        int med = 0;
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            if (i == 0) {
                med = nums[i];
            }
            else{
                if (nums[i] >= med){
                    right.add(nums[i]);
                }
                else{
                    left.add(-nums[i]);
                }
                med = rebalance(left, right, med);
            }
            result[i] = med;
        }
        return result;
    }
    
    private int rebalance(Queue<Integer> left, Queue<Integer> right, int med){
        if (left.size() > right.size()){
            right.add(med);
            med = -left.poll();
        }
        else if (left.size() + 2 <= right.size()){
            left.add(-med);
            med = right.poll();
        }
        return med;
    }
}