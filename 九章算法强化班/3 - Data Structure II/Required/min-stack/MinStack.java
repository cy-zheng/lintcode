import java.util.*;

public class MinStack {

    private Stack<Integer> stack;
    private PriorityQueue<Integer> pq;

    public MinStack() {
        // do initialize if necessary
        this.stack = new Stack<Integer>();
        this.pq = new PriorityQueue<Integer>();
    }

    public void push(int number) {
        // write your code here
        stack.push(number);
        pq.add(number);
    }

    public int pop() {
        // write your code here
        int result = stack.pop();
        pq.remove(result);
        return result;
    }

    public int min() {
        // write your code here
        return pq.peek();
    }
}
