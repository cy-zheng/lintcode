import java.util.*;

class TrieNode{
    public char val;
    public Map<Character, TrieNode> next = new HashMap<>();
    public boolean isEnd;
    public TrieNode(char val){
        this.val = val;
    }
}


public class WordDictionary {
    
    private TrieNode root = new TrieNode('\n');

    // Adds a word into the data structure.
    public void addWord(String word) {
        // Write your code here
        addHelper(word, root);
    }
    
    private void addHelper(String word, TrieNode root){
        if (word.equals("")){
            root.isEnd = true;
        }
        else{
            if (!root.next.containsKey(word.charAt(0))){
                root.next.put(word.charAt(0), new TrieNode(word.charAt(0)));
            }
            addHelper(word.substring(1), root.next.get(word.charAt(0)));
        }
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        // Write your code here
        return searchHelper(word, root);
    }
    
    private boolean searchHelper(String word, TrieNode root){
        if (word.equals("")){
            return root.isEnd;
        }
        else if(word.charAt(0) == '.'){
            boolean result = false;
            for (Character i : root.next.keySet()){
                result |= searchHelper(word.substring(1), root.next.get(i));
            }
            return result;
        }
        else{
            if (!root.next.containsKey(word.charAt(0))){
                return false;
            }
            return searchHelper(word.substring(1), root.next.get(word.charAt(0)));
        }
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");