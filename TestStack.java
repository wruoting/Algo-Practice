public class TestStack{
  static class Node {
    int data;
    Node next;
    public Node(int data){
      this.data = data;
      next = null;
    }
  }
  static class Stack {
    Node top;
    int d;
    void push(int i){
      Node t = new Node(i);
      t.next = top;
      top = t;
      return;
    }
    Node pop() {
      if(top != null) {
        Node t = top.next;
        d = (Integer) top.data;
        top = t;
        return top;
      }
      return null;
    }

  }
  public static void main(String args[]) {
    Stack stack = new Stack();
    Node helpMe = new Node(1);
    stack.push(8);
    stack.push(5);
    stack.push(6);
    stack.pop();
    System.out.println(stack.top.data);
  }
}
