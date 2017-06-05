import java.util.*;
public class Solution {
    /**
     * @param s: a string
     * @return: an integer
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        int result = 0;
        if (s == null || s.length() == 0){
            return result;
        }
        Map<Character, Integer> map = new HashMap<>();
        int j = 0;
        for (int i = 0; i < s.length(); i++){
            if (i > 0){
                map.put(s.charAt(i - 1), map.get(s.charAt(i - 1)) - 1);
                if (map.get(s.charAt(i - 1)) == 0){
                    map.remove(s.charAt(i - 1));
                }
            }
            while(j < s.length()){
                if (map.containsKey(s.charAt(j))){
                    break;
                }
                else {
                    map.put(s.charAt(j), 1);
                    if (map.entrySet().size() > result){
                        result = map.entrySet().size();
                    }
                    j++;
                }
            }
        }
        return result;
    }
}