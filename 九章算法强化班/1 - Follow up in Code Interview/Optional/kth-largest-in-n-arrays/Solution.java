import java.util.*;

class Item{
    public int val, index, array;
    public Item(int val, int index, int array){
        this.val = val;
        this.index = index;
        this.array = array;
    }
}

class ItemComparator implements Comparator<Item>{
    public int compare(Item a, Item b){
        return b.val - a.val;
    }
}

public class Solution {
    /**
     * @param arrays a list of array
     * @param k an integer
     * @return an integer, K-th largest element in N arrays
     */
    public int KthInArrays(int[][] arrays, int k) {
        // Write your code here
        PriorityQueue<Item> pq = new PriorityQueue<>(k, new ItemComparator());
        for (int i = 0; i < arrays.length; i++){
            Arrays.sort(arrays[i]);
            if (arrays[i].length > 0){
                pq.add(new Item(arrays[i][arrays[i].length - 1], arrays[i].length - 1, i));
            }
        }
        for (int i = 0; i < k - 1; i++){
            Item item = pq.poll();
            if (item.index > 0){
                pq.offer(new Item(arrays[item.array][item.index - 1], item.index - 1, item.array));
            }
        }
        return pq.peek().val;
    }
}