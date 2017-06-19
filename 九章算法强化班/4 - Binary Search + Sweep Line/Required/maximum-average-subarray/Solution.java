public class Solution {
    /**
     * @param nums an array with positive and negative numbers
     * @param k an integer
     * @return the maximum average
     */
    public double maxAverage(int[] nums, int k) {
        // Write your code here
        double left = 0;
        int max = Integer.MIN_VALUE;
        for (int n : nums){
            left += n;
            max = Math.max(max, n);
        }
        left = left / nums.length;
        double right = max;
        
        while (right - left > 1e-7){
            double mid = (left + right) / 2;
            if (check(nums, k, mid)){
                left = mid;
            }
            else{
                right = mid;
            }
        }
        return left;
    }
    
    private boolean check(int[] nums, int k, double mid){
        double[] prefix = new double[nums.length + 1];
        double minPre = 0;
        for (int i = 0; i < nums.length; i++){
            // prefix 减去平均值
            // 转换为是否存在一个长度大于k的子数组和>0
            prefix[i + 1] = prefix[i] + nums[i] - mid;
            if (i >= k - 1){
                minPre = Math.min(minPre, prefix[i - k + 1]);
                if (prefix[i + 1] - minPre >= 0){
                    return true;
                }
            }
        }
        return false;
    }
}