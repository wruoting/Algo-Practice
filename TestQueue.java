public class TestQueue{
  public static class Node {
    int data;
    Node next;
    public Node(int data) {
      this.data = data;
      next = null;
    }
  }

  Node front;
  Node rear;
  void enqueue(int key) {
    Node temp = new Node(key);
    if(this.rear == null) {
      this.rear = temp;
      this.front = this.rear;
      return;
    }
    this.rear.next = temp;
    this.rear = temp;
  }

  Node dequeue() {
    if(this.front == null) {
      return null;
    }
    Node temp = this.front;
    this.front = this.front.next;
    if(this.front == null) {
      this.rear = null;
    }
    return temp;
  }
  public TestQueue() {
    this.front = this.rear = null;
  }


  public static void main(String args[]) {
    TestQueue newQ = new TestQueue();
    newQ.enqueue(5);
    newQ.enqueue(6);
    newQ.dequeue();
    System.out.println(newQ.dequeue().data);
  }

}
