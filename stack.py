class Node(object):
    def __init__(self, value):
        self.next = None
        self.val = value

class Stack(object):
    def __init__(self):
        self.stack = None
    def push(self, i):
        temp = Node(i)
        if self.stack is None:
            self.stack = temp
        else:
            temp.next = self.stack
            self.stack = temp
    def pop(self):
        temp = self.stack.val
        self.stack = self.stack.next
        return temp
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())