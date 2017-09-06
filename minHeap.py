# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:01:00 2017

@author: A-Singleton
"""

class minHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0
        
    def insert(self, key):
        self.heaplist.append(key)
        self.currentSize += 1
        self.percUp(self.currentSize)
 
    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2] :
                holder_val = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i//2]
                self.heaplist[i//2] = holder_val
            i = i//2
       
    def percDown(self, i):
        while i*2 <= (self.currentSize):
            next_min = self.minChild(i)
            if(self.heaplist[i] > self.heaplist[next_min]):
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[next_min]
                self.heaplist[next_min] = tmp
            i = next_min
            
    def minChild(self, i):
        if 2*i+1 > self.currentSize():
            return 2*i
        else:
            if (self.heaplist[2*i+1] > self.heaplist[2*i]): 
                return 2*i
            else:
                return 2*i+1
        
    def del_min(self):
        minimum = self.heaplist[1]
        self.currentSize -= 1
        #self.heaplist[1] = self.heaplist.pop()
        self.heaplist[1] = self.heaplist[self.currentSize-1]
        self.heaplist.pop()
        self.percDown(1)
        return minimum
     
    def remove_ith_element(self, key):
        counter = 1
        while (self.heaplist[counter] is not key):
            counter+=1
        self.heaplist[counter] = self.heaplist[-1]
        self.heaplist.pop()
        self.currentSize -= 1
        self.percDown(counter)
        
    def print_min(self):
        return print(self.heaplist[1])
    
def main():
    pass
            
if __name__ == '__main__':
    main()