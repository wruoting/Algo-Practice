class Node(object):
	def __init__(self, value):
		self.next = None
		self.val = value

class TreeNode(object):
	def __init__(self, value):
		self.val = value
		self.right = None
		self.left = None

class Queue(object):
	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, value):
		if self.rear is None:
			self.rear = Node(value)
			self.front = self.rear
		else:
			self.rear.next = Node(value)
			self.rear = self.rear.next

	def dequeue(self):
		if self.front is None:
			self.rear = None
			return None
		else:
			temp = self.front.val
			self.front = self.front.next
			if self.front is None:
				self.rear = None
			return temp

class Stack(object):
	def __init__(self):
		self.head = None
	def push(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			temp = Node(value)
			temp.next = self.head
			self.head = temp

	def pop(self):
		if self.head is None:
			return None
		else:
			temp = self.head.val
			self.head = self.head.next
			return temp

	def peek(self):
		if self.head is None:
			return None
		else:
			return self.head.val


def recursive_add(treeNode, stack_imp):
	if treeNode is None:
		return
	if treeNode.right is not None:
		stack_imp.push(treeNode.right)	
	if treeNode.left is not None:
		stack_imp.push(treeNode.left)
	if treeNode is not None:
		print(treeNode.val)

	temp = stack_imp.pop()

	return recursive_add(temp, stack_imp)

def recursive_queue_add(treeNode, queue_imp):
	if treeNode is None:
		return
	if treeNode.left is not None:
		queue_imp.enqueue(treeNode.left)
	if treeNode.right is not None:
		queue_imp.enqueue(treeNode.right)
	if treeNode.val is not None:
		print(treeNode.val)
	temp = queue_imp.dequeue()
	recursive_queue_add(temp, queue_imp)

def depthFirst(treeNode):
	stack_imp = Stack()
	recursive_add(treeNode, stack_imp)	


def breadthFirst(treeNode):
	queue_imp = Queue()
	recursive_queue_add(treeNode, queue_imp)

a = Queue()
b = Stack()

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(1)
bst.right = TreeNode(7)
bst.right.right = TreeNode(10)
bst.right.left = TreeNode(6)

# 5
# 3, 7
# 1, None, 6, 10

depthFirst(bst)
print('----')			
breadthFirst(bst)