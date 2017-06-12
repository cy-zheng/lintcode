/**
 * Your Trie object will be instantiated and called as such:
 * Trie trie = new Trie();
 * trie.insert("lintcode");
 * trie.search("lint"); will return false
 * trie.startsWith("lint"); will return true
 */
import java.util.*;
class TrieNode {
    // Initialize your data structure here.
    public char val;
    public Map<Character, TrieNode> next = new HashMap<>();
    public boolean isEnd;

    public TrieNode(char val) {
        this.val = val;
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode('\n');
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        insertHelper(word, root);
    }

    private void insertHelper(String word, TrieNode root){
        if (word.equals("")){
            root.isEnd = true;
        }
        else{
            if (!root.next.containsKey(word.charAt(0))){
                root.next.put(word.charAt(0), new TrieNode(word.charAt(0)));
            }
            insertHelper(word.substring(1), root.next.get(word.charAt(0)));
        }
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        return searchHelper(word, root);
    }

    private boolean searchHelper(String word, TrieNode root){
        if (word.equals("")){
            return root.isEnd;
        }
        else{
            if (!root.next.containsKey(word.charAt(0))){
                return false;
            }
            return searchHelper(word.substring(1), root.next.get(word.charAt(0)));
        }
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        return startsWithHelper(prefix, root);
    }

    private boolean startsWithHelper(String word, TrieNode root){
        if (word.equals("")){
            return true;
        }
        else{
            if (!root.next.containsKey(word.charAt(0))){
                return false;
            }
            return startsWithHelper(word.substring(1), root.next.get(word.charAt(0)));
        }
    }
}