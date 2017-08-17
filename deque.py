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

def max_of_subarrays(arr, k):
           
    if(k > len(arr) or k < 1):
        return None
    
    if arr is None:
        return None

    deque = Deque()    
    for i in range(0, k):
        deque.insert_front(arr[i])
        
    right_arr_index = k - 1
    while(right_arr_index < len(arr)):

        max_val = -1*float("inf")
        for val in deque.deque:
            if val > max_val:
                max_val = val
                
        right_arr_index += 1
        if (right_arr_index is not len(arr)):
            deque.pop_back()
            deque.insert_front(arr[right_arr_index])           
        
        print(max_val)


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

def sum_of_min_and_max_of_all_contiguous_subarrays(arr, k):
    
    # Prevent improper inputs
    if k > len(arr) or k < 1:
        return None
    
    if arr is None:
        return None
    
    deque = Deque()   
    for i in range(0, k):
        deque.insert_front(arr[i])
        
    right_arr_index = k-1
    result_list = []
    run_sum = 0
    
    while(right_arr_index < len(arr)):
        
        max_value = -1*float('inf')
        for item in deque.deque:
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
                
    

def main():
    arr_1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    arr_2 = [2, 5, -1, 7, -3, -1, -2]
    
    k_1 = 3
    k_2 = 4
	
    max_of_subarrays(arr_1, k_1)
    sum_of_min_and_max_of_all_contiguous_subarrays(arr_2, k_2)
    
if __name__ == '__main__':
    main()
    

