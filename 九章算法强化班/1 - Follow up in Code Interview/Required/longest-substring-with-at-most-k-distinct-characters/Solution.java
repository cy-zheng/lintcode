public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        int result = 0;
        if (s == null || s.length() == 0){
            return result;
        }
        Map<Character, Integer> map = new HashMap<>();a
        int j = 0;
        for (int i = 0; i < s.length(); i++){
            boolean flag = false;
            if (i > 0){
                map.put(s.charAt(i - 1), map.get(s.charAt(i - 1)) - 1);
                if (map.get(s.charAt(i - 1)) == 0){
                    map.remove(s.charAt(i - 1));
                }
                flag = true;
            }
            while(j < s.length()){
                if(!flag){
                    if (map.containsKey(s.charAt(j))){
                        map.put(s.charAt(j), map.get(s.charAt(j)) + 1);
                    }
                    else{
                        map.put(s.charAt(j), 1);
                    }
                }
                else {
                    flag = false;
                }
                if (map.entrySet().size() > k){
                    break;
                }
                else {
                    if (j - i + 1 > result){
                        result = j - i + 1;
                    }
                    j++;
                }
            }
        }
        return result;
    }
}