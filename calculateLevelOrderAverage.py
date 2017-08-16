# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:56:15 2017

@author: Duwan_000
"""

class BST:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

     
    def insert(self, data):       
        if data >= self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
                
        else:        
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
                
                
    def preOrderTraversal(self):
        print(self.data)
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()
            
        
    def rowAvgCalculator(self):
        q1=[]
        q2=[]
        row_avg = []
        run_sum = 0
        n = 0
        
        q1.append(self)

        while(len(q1) != 0 or len(q2) != 0):
            while(len(q1) != 0):
                
                node = q1.pop()
                run_sum += node.data
                n += 1
                
                if node.left:
                    q2.insert(0, node.left)
                    
                if node.right:
                    q2.insert(0, node.right)
            
            row_avg.append(run_sum/n)
            run_sum = 0
            n = 0
            
            q1 = q2
            q2 = []
        
        for level in row_avg:
            print(level)
            
        return row_avg
                
    
def main():            
    myTree = BST(7)            
    myTree.insert(10)
    myTree.insert(5)
    myTree.insert(11)
    myTree.insert(6)
    myTree.insert(4)
    myTree.insert(9)
    myTree.insert(3)
    
    myTree.preOrderTraversal()
    
    avg_List = myTree.rowAvgCalculator()

if __name__ == '__main__':
    main()
        