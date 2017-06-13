public class ConnectingGraph {

    private int[] father = null;

    public ConnectingGraph(int n) {
        // initialize your data structure here.
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
        father[a_f] = b_f;

    }

    public boolean  query(int a, int b) {
        // Write your code here
        int a_f = find(a - 1);
        int b_f = find(b - 1);
        return a_f == b_f;
    }
}