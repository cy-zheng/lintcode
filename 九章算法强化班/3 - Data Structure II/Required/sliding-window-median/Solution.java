import java.util.*;

public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: The median of the element inside the window at each moving.
     */
    public ArrayList<Integer> medianSlidingWindow(int[] nums, int k) {
        // write your code here
        // if k is even, return (k / 2) - 1 th
        // that means left.size() == right.size(), 
        // or left.size() + 1 == right.size()
        if (k == 0 || nums.length < k){
            return new ArrayList<Integer>();
        }
        // k = 1, return
        if (k == 1){
            ArrayList<Integer> result = new ArrayList<Integer>();
            for (int i : nums){
                result.add(i);
            }
            return result;
        }
        
        ArrayList<Integer> result = new ArrayList<Integer>();
        PriorityQueue<Integer> left = new PriorityQueue<Integer>();
        PriorityQueue<Integer> right = new PriorityQueue<Integer>();
        int med = -123456;
        
        for (int i = 0; i < nums.length; i++){
            if (med == -123456){
                med = nums[i];
                continue;
            }
            if (i >= k){
                if (med == nums[i - k]){    // med need to remove
                    if (left.size() == right.size()){
                        med = -left.poll();
                    }
                    else{
                        med = right.poll();
                    }
                }
                else{
                    if (nums[i - k] < med){
                        left.remove(-nums[i - k]);
                    }
                    else{
                        right.remove(nums[i - k]);
                    }
                }
            }
            med = rebalance(left, right, med);
            if (nums[i] >= med){
                right.offer(nums[i]);
            }
            else{
                left.offer(-nums[i]);
            }
            med = rebalance(left, right, med);
            if (i >= k - 1){
                result.add(med);  
            }
        }
        return result;
    }
    private int rebalance(PriorityQueue<Integer> left, PriorityQueue<Integer> right,
            int med){
        if (right.size() - 1 > left.size()){
            left.offer(-med);
            med = right.poll();
        }
        else if (left.size() > right.size()){
            right.offer(med);
            med = -left.poll();
        }  
        return med;
    }
}
