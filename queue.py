class Node(object):
    def __init__(self, value):
        self.next = None
        self.val = value
        
class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, key):
        temp = Node(key)
        if self.rear is None:
            self.rear = temp
            self.front = self.rear
        else:
            self.rear.next = temp
            self.rear = self.rear.next
            
    def dequeue(self):
        if self.front is None:
            self.rear = None
            return None
        temp = self.front
        self.front = self.front.next
        return temp.val

testQueue = Queue()
testQueue.enqueue(1)
testQueue.enqueue(2)
testQueue.enqueue(3)
print(testQueue.dequeue())
print(testQueue.dequeue())