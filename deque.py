"""
Let's work on double-ended queues, which are a special type of queue for which you can
insert and pop at both sides.  See https://en.wikipedia.org/wiki/Double-ended_queue

Exercise 1: Implement a deque (short for double-ended queue):
"""

class Deque(object):

	def __init__(self):
		"""
		Initializes a deque with no elements
		"""

	def insert_front(self, value):
		"""
		Inserts 'value' at the front of the deque
		"""

	def insert_back(self, value):
		"""
		Inserts 'value' at the back of the deque
		"""

	def pop_front(self):
		"""
		Returns the value at the front of the deque, and removes it.
		Returns None if the deque is empty.
		"""

	def pop_back(self):
		"""
		Returns the value at the back of the deque, and removes it.
		Returns Non if the deque is empty.
		"""

"""
Exercise 2: I found this one at http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Try to solve this one with your Deque class above.  Feel free to add new methods to it if you'd like. 
"""

def max_of_subarrays(arr):
	pass

"""
Exercise 3: I found this one at http://www.geeksforgeeks.org/sum-minimum-maximum-elements-subarrays-size-k/

Given an array of both positive and negative integers, the task is to compute sum of minimum and maximum
elements of all contiguous sub-array of size k.

E.g.
Input : arr[] = {2, 5, -1, 7, -3, -1, -2}  
        K = 4
Output : 18
Explanation : Subarrays of size 4 are : 
     {2, 5, -1, 7},   min + max = -1 + 7 = 6
     {5, -1, 7, -3},  min + max = -3 + 7 = 4      
     {-1, 7, -3, -1}, min + max = -3 + 7 = 4
     {7, -3, -1, -2}, min + max = -3 + 7 = 4   
     Sum of all min & max = 6 + 4 + 4 + 4 
                          = 18
"""

def sum_of_min_and_max_of_all_contiguous_subarrays(arr):
	pass


