"""
Let's work on double-ended queues, which are a special type of queue for which you can
insert and pop at both sides.  See https://en.wikipedia.org/wiki/Double-ended_queue

Exercise 1: Implement a deque (short for double-ended queue):
"""

class Deque(object):

    def __init__(self):
        self.deque = []

    def insert_front(self, value):
        self.deque.append(value)

    def insert_back(self, value):
        self.deque.insert(0,value)

    def pop_front(self):
        if self.deque:
            return self.deque.pop()
        else:
            return None


    def pop_back(self):
        if self.deque:
            return self.deque.pop(0)
        else:
            return None
        
    def size(self):
        return len(self.deque)
        
    def peek_back(self):
        return self.deque[0]

    def max(self):
    	return max(self.deque)
        

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

#Brute force solution
#
def max_of_subarrays(arr, k):
           
    if(k > len(arr) or k < 1):
        return None
    
    if arr is None:
        return None

    deque = Deque()    
    for i in range(0, k): # you can just use range(k)
        deque.insert_front(arr[i])
        
    right_arr_index = k - 1

    """
	Something that's nice for loops in which you need to know the index is Python's enumerate builtin. See
	https://docs.python.org/2.3/whatsnew/section-enumerate.html

	You then could've said something along the lines of:
	for ind, val in arr[k-1:]:
		...
    """
    while(right_arr_index < len(arr)):

    	"""
		This would've been a nice spot to add a "max" method to Deque.  I went ahead and added it, using Python's
		"max" built-in.

		It's worth familiarizing yourself with Python 2's built-ins for situations like these.  See
		https://docs.python.org/2/library/functions.html
    	"""
        max_val = -1*float("inf")  
        for val in deque.deque:
            if val > max_val:
                max_val = val
                
        right_arr_index += 1
        if (right_arr_index is not len(arr)):
            deque.pop_back()
            deque.insert_front(arr[right_arr_index])           
        
        print(max_val)


#Optimized Solution
#
def max_of_subarrays_n_time(arr, k):
    
    if(k > len(arr) or k < 1):
        return None
    
    if arr is None:
        return None
    
    deque_of_indecies = Deque()
    max_of_subarrays = []
    
    # Fill deque from first subarray
    for i in range(0, k):  # Just say range(k)
    	"""
		You should never access internals of a class, as in deque_of_indecies.deque.  In fact, it's customary
		to prefix fields with a "_" to make that obvious, as in deque_of_indecies._deque.  You should implement
		a method on the class to do the thing that you want, which you seem to have done in peek_back.

		The reason that it's bad to access class internals is that the writers of the class should be able to
		change the internal implementation without affecting dependers.  Maintainers of a class are only
		responsible for its API, that is; its public methods.
    	"""
        while(deque_of_indecies.size() > 0 and arr[deque_of_indecies.deque[-1]] 
        <= arr[i]):
            
            deque_of_indecies.pop_front()
        deque_of_indecies.insert_front(i)
    
    print(arr[deque_of_indecies.peek_back()])
    max_of_subarrays.append(arr[deque_of_indecies.peek_back()])
    
    # Perform alg on remaining array
    for i in range(k, len(arr)):
        
        #shift over one and remove if subarray has moved past the index
        if ( deque_of_indecies.deque[0] <= i-k ):
            deque_of_indecies.pop_back()
           
        while(deque_of_indecies.size() > 0 and arr[deque_of_indecies.deque[-1]]
        <= arr[i]):
            
            deque_of_indecies.pop_front()
        deque_of_indecies.insert_front(i)
            
        print(arr[deque_of_indecies.peek_back()])
        max_of_subarrays.append(arr[deque_of_indecies.peek_back()])    
        
    return max_of_subarrays

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
# Brute Force Solution
# 
def sum_of_min_and_max_of_all_contiguous_subarrays(arr, k):
    
    # Prevent improper inputs
    if k > len(arr) or k < 1:
        return None  # Throw an exception on malformed input.
        # raise Exception("lenght of subarrays must be greater than zero and smaller than the length of the array")
    
    if arr is None:
        return None
    
    deque = Deque() # seems like you could just use a plain list here
    for i in range(0, k):
        deque.insert_front(arr[i])
        
    right_arr_index = k-1
    result_list = []
    run_sum = 0  # <- good variable naming here, and throughout this solution.
    
    while(right_arr_index < len(arr)): # Use a 'for' loop with enumerate here.
        
        # Use built-in min and max functions: https://docs.python.org/2/library/functions.html
        max_value = -1*float('inf')
        for item in deque.deque:  # don't access class internals - implement __iter__, see http://anandology.com/python-practice-book/iterators.html
            if item > max_value:
                max_value = item
        
        min_value = float('inf')
        for item in deque.deque:
            if item < min_value:
                min_value = item
        
        right_arr_index += 1
        if (right_arr_index is not len(arr)):
            deque.pop_back()
            deque.insert_front(arr[right_arr_index])
        
        result_list.append(max_value + min_value)
        run_sum += (max_value + min_value)

    print(run_sum)
                
    
# Optimized Solution
#
def sum_of_min_and_max_of_all_contiguous_subarrays_n_time(arr, k):
    """ 
    I don't really understand what's going on here - could you give me a brief
    explination of your approach here? I think it's best if you generally
    write some comments to describe your approach when we're working together
    over GitHub.
    """


    if(k > len(arr) or k < 1):
        return None
    
    if arr is None:
        return None
    
    min_deque = Deque()
    max_of_subarrays = max_of_subarrays_n_time(arr, k) # cool :)
    min_of_subarrays = []
      
    for i in range(0, k):
        while(min_deque.size() > 0 and arr[ min_deque.deque[-1]]
        >= arr[i]):
            
             min_deque.pop_front()
        min_deque.insert_front(i)
    
    print(arr[min_deque.peek_back()])
    min_of_subarrays.append(arr[min_deque.peek_back()])
    
    # Perform alg on remaining array
    for i in range(k, len(arr)):
        
        #shift over one and remove if subarray has moved past the index
        if (  min_deque.deque[0] <= i-k ):
             min_deque.pop_back()
           
        while( min_deque.size() > 0 and arr[ min_deque.deque[-1]]
        >= arr[i]):
             min_deque.pop_front()
        min_deque.insert_front(i)
            
        print(arr[min_deque.peek_back()])
        min_of_subarrays.append(arr[min_deque.peek_back()])
        
    print(sum(max_of_subarrays) + sum(min_of_subarrays))
    return (sum(max_of_subarrays) + sum(min_of_subarrays))


def main():
    arr_1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    arr_2 = [2, 5, -1, 7, -3, -1, -2]
    
    k_1 = 3
    k_2 = 4
	
    max_of_subarrays(arr_1, k_1)
    sum_of_min_and_max_of_all_contiguous_subarrays(arr_2, k_2)
    
    max_of_subarrays_n_time(arr_1, k_1)
    sum_of_min_and_max_of_all_contiguous_subarrays_n_time(arr_2, k_2)
    
if __name__ == '__main__':
    main()
    

