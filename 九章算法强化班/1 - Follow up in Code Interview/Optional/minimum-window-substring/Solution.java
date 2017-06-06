import java.util.*;

public class Solution {
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    public String minWindow(String source, String target) {
        // write your code
        if (source.length() == 0 || target.length() == 0) return "";
        int startIndex = 0;
        int endIndex = 0;
        Map<Character, Integer> targetMap = new HashMap<>();
        Map<Character, Integer> sourceMap = new HashMap<>();
        for (int i = 0; i < target.length(); i++){
            if (!targetMap.containsKey(target.charAt(i))){
                targetMap.put(target.charAt(i), 1);
            }
            else{
                targetMap.put(target.charAt(i), targetMap.get(target.charAt(i)) + 1);
            }
        }
        while(endIndex < source.length()){
            if (!sourceMap.containsKey(source.charAt(endIndex))){
                sourceMap.put(source.charAt(endIndex), 1);
            }
            else{
                sourceMap.put(source.charAt(endIndex), sourceMap.get(source.charAt(endIndex)) + 1);
            }
            if (testHash(sourceMap, targetMap)){
                break;
            }
            endIndex++;
        }
        if (endIndex == source.length()){
            return "";
        }
        while(startIndex <= endIndex){
            sourceMap.put(source.charAt(startIndex), sourceMap.get(source.charAt(startIndex)) - 1);
            if (sourceMap.get(source.charAt(startIndex)) == 0){
                sourceMap.remove(source.charAt(startIndex));
            }
            if (!testHash(sourceMap, targetMap)){
                break;
            }
            startIndex++;
        }
        return source.substring(startIndex, endIndex + 1);
    }
    
    private boolean testHash(Map<Character, Integer> sourceMap, Map<Character, Integer> targetMap){
        for (Character key : targetMap.keySet()){
            if (!sourceMap.containsKey(key) || sourceMap.get(key) < targetMap.get(key)) {
                return false;
            }
        }
        return true;
    }
}