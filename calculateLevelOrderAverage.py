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
        level_to_be_averaged = []
        child_nodes = []
        row_avg = []
        
        level_to_be_averaged.append(self)

        while(level_to_be_averaged):
            run_sum = 0
            n = 0
           
            while(level_to_be_averaged):
                
                node = level_to_be_averaged.pop()
                run_sum += node.data
                n += 1
                
                if node.left:
                    child_nodes.insert(0, node.left)
                    
                if node.right:
                    child_nodes.insert(0, node.right)
            
            row_avg.append(float(run_sum/n))
            
            level_to_be_averaged = child_nodes
            child_nodes = []
        
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
    myTree.insert(8.7)
    myTree.insert(3)
    
    myTree.preOrderTraversal()
    
    myTree.rowAvgCalculator()

if __name__ == '__main__':
    main()
        