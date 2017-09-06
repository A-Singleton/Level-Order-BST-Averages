# -*- coding: utf-8 -*-
"""
@author: A-Singleton
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

    def peek_front(self):
        return self.deque[-1]
    
    def max(self):
    	return max(self.deque)
    
    def min(self):
        return min(self.deque)
     

"""
Exercise 2: I found this one at http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6 
"""

#Brute force solution
#

def max_of_subarrays(arr, k):
           
    # Prevent improper inputs
    if arr is None:
        raise ValueError(" Input Array must not be 'None' ")
        
    if k is None:
        raise ValueError(" Subarrays 'k' must not be 'None' ")
        
    if k > len(arr) or k < 1:
        raise ValueError(" Length of subarrays 'k' must be > 0 and < len(arr) ")

    # Could optionally initialize a given list as the intital deque.
    deque = Deque()    
    for i in range(k): 
        deque.insert_front(arr[i])
    
    max_list = []
    for i, val in enumerate(arr[k-1:]): # Should I still use enumerate if I dont directly use the i var?
        
        deque.pop_back()
        deque.insert_front(val) 
        
        max_sub_array = deque.max()       
        
#        print('max_sub_array')
#        print(max_sub_array)
        max_list.append(max_sub_array)
        
    for x in max_list:    
        print(x, end=' ')


#Optimized Solution
#
    
def max_of_subarrays_n_time(arr, k):
    
   # Prevent improper inputs
    if arr is None:
        raise ValueError(" Input Array must not be 'None' ")
        
    if k is None:
        raise ValueError(" Subarrays 'k' must not be 'None' ")
        
    if k > len(arr) or k < 1:
        raise ValueError(" Length of subarrays 'k' must be > 0 and < len(arr) ")
    
    deque_of_indecies = Deque()
    max_of_subarrays = []
    
    # Fill deque from first subarray
    for i in range(k): 
 
        while(deque_of_indecies.size() > 0 and arr[deque_of_indecies.peek_front()] 
        <= arr[i]):
            
            deque_of_indecies.pop_front()
        deque_of_indecies.insert_front(i)
    
    max_of_subarrays.append(arr[deque_of_indecies.peek_back()])
    
    # Perform alg on remaining array
    for i in range(k, len(arr)):
        
        #shift over one and remove if subarray has moved past the index
        if ( deque_of_indecies.peek_back() <= i-k ):
            deque_of_indecies.pop_back()
           
        while(deque_of_indecies.size() > 0 and arr[deque_of_indecies.peek_front()]
        <= arr[i]):
            
            deque_of_indecies.pop_front()
        deque_of_indecies.insert_front(i)
            
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
    if arr is None:
        raise ValueError(" Input Array must not be 'None' ")
        
    if k is None:
        raise ValueError(" Subarrays 'k' must not be 'None' ")
        
    if k > len(arr) or k < 1:
        raise ValueError("Length of subarrays 'k' must be > 0 and < len(arr)")
        
    deque = Deque() # seems like you could just use a plain list here 
    for i in range(k):  # ^^^ I agree since the above class is really just a list, e.g. insert_back() takes n time rather than O(1)
        deque.insert_front(arr[i]) # Would I use the above class or just import deque which actually supports constant time ops?
        
    result_list = []
    run_sum = 0 
    
    for i, val in enumerate(arr[k-1:]): 
    
        deque.pop_back()
        deque.insert_front(val) 
        
        max_sub_array = deque.max()               
        min_sub_array = deque.min()       

        result_list.append(max_sub_array + min_sub_array)
        run_sum += (max_sub_array + min_sub_array)

    print("")
    print("Final Running Sum:")
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

# I adapted method 3 from this article into python:
    # http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# I was resarching optimal ways to solve this problem and I didn't get it at 
    # first but figured it out and implemented it, it's pretty clever.

    # Prevent improper inputs
    if arr is None:
        raise ValueError(" Input Array must not be 'None' ")
        
    if k is None:
        raise ValueError(" Subarrays 'k' must not be 'None' ")
        
    if k > len(arr) or k < 1:
        raise ValueError("Length of subarrays 'k' must be > 0 and < len(arr)")
    
    min_deque = Deque()
    max_of_subarrays = max_of_subarrays_n_time(arr, k) # cool :)
    min_of_subarrays = []
      
    for i in range(k):
        while(min_deque.size() > 0 and arr[ min_deque.peek_front()]
        >= arr[i]):
            
             min_deque.pop_front()
        min_deque.insert_front(i)
    
    min_of_subarrays.append(arr[min_deque.peek_back()])
    
    # Perform alg on remaining array
    for i in range(k, len(arr)):
        
        #shift over one and remove if subarray has moved past the index
        if (  min_deque.peek_back() <= i-k ):
             min_deque.pop_back()
           
        while( min_deque.size() > 0 and arr[ min_deque.peek_front()]
        >= arr[i]):
             min_deque.pop_front()
        min_deque.insert_front(i)
            
        min_of_subarrays.append(arr[min_deque.peek_back()])
        
#    print(sum(max_of_subarrays) + sum(min_of_subarrays))


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