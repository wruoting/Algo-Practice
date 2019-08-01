# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

	def addToEnd(self, list_t, value):
	    if list_t.next is None:
	        list_t.next = ListNode(value)
	    else:
	        headval = list_t
	        while headval.next is not None:
	            headval = headval.next
	        headval.next = ListNode(value)
	    return list_t

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		answer = None
		this_tens = 0
		while l1 is not None or l2 is not None or this_tens != 0:
			total_sum = 0
			if l1 is not None:
				total_sum = l1.val
			if l2 is not None:
				total_sum += l2.val
			if this_tens > 0:
				this_digit = (total_sum + this_tens) % 10
				this_tens = ((total_sum + this_tens) - this_digit)/10
			else:
				this_digit = (total_sum) % 10
				this_tens = (total_sum - this_digit)/10
			if l1 is not None:
				l1 = l1.next
			if l2 is not None:
				l2 = l2.next
			if answer is None:
				answer = ListNode(this_digit)
			else:
				answer = self.addToEnd(answer, this_digit)
		return answer