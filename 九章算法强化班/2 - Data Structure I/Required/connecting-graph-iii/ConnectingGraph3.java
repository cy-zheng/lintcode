public class ConnectingGraph3 {

    private int[] father = null;
    private int count = 0;

    public ConnectingGraph3(int n) {
        // initialize your data structure here.
        this.count = n;
        father = new int[n];
        for(int i = 0; i < n; i++){
            father[i] = i;
        }
    }

    private int find(int a){
        if (father[a] == a){
            return a;
        }
        int result = find(father[a]);
        father[a] = result;
        return result;
    }

    public void connect(int a, int b) {
        // Write your code here
        int a_f = find(a - 1);
        int b_f = find(b - 1);
        if (a_f != b_f){
            count--;
        }
        father[a_f] = b_f;
    }

    public int query() {
        // Write your code here
        return count;
    }
}