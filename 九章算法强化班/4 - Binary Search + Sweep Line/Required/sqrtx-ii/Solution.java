public class Solution {
    /**
     * @param x a double
     * @return the square root of x
     */
    public double sqrt(double x) {
        // Write your code here
        double left = 0;
        // x < 1? 
        double right = x < 1 ? 1 : x;
        double delta = 1e-12;
        
        while (left + delta < right){
            double mid = (left + right) / 2;
            if (mid * mid < x){
                left = mid;
            }
            else{
                right = mid;
            }
        }
        return left;
    }
}