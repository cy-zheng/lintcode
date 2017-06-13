class Solution {
    /*
     * @param k an integer
     * @param nums an integer array
     * @return kth smallest element
     */
    public int kthSmallest(int k, int[] nums) {
        // write your code here
        return quickSelect(nums, 0, nums.length - 1, k);
    }

    private int quickSelect(int[] nums, int start, int end, int k){
        if (start >= end){
            return nums[start];         //区间只有一个数，直接返回
        }
        int pivot = nums[(start + end) / 2];
        int i = start;
        int j = end;
        while(i <= j){                           //i<=j，有等号
            while(i <= j && nums[i] < pivot){         //和pivot比较没有等号
                i++;
            }
            while(i <= j && nums[j] > pivot){
                j--;
            }
            if(i <= j){
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i++;                             //两个同时++ --
                j--;
            }
        }
        if (j - start >= k - 1){              //答案落在0~j区间
            return quickSelect(nums, start, j, k);
        }
        else if (i - start <= k - 1){                //答案落在i~end区间，注意k
            return quickSelect(nums, i, end, k - i + start);
        }
        else {
            return nums[j + 1];             //j和i中间隔了一个，它恰好是答案
        }
    }
}