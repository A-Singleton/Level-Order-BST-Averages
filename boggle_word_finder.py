# -*- coding: utf-8 -*-
"""
@author: A-Singleton
"""

"""
    Returns all valid words of size n in the boggle_board that are in the dictionary
"""
        
class Boggle:
    def __init__(self, boggle_board, n, dictionary):
        self.boggle_board = boggle_board
        self.n = n
        self.dictionary = dictionary
        self.found_words = []
    
    def search_from_square(self, start_i, start_j, path=[], string_path=[]):
        
    # Explores all possible paths from the letter in the start element
        start = [self.boggle_board[start_i][start_j], start_i, start_j]

    # Keep a path of dfs in order to backtrack and explore more possibilities
        path = path + [start]
        string_path = string_path + [start[0]]
        current_word = "".join(string_path)

    # Test word candidate for proper length and if not found already 
        if len(current_word) is self.n:
            if (current_word in self.dictionary) and (current_word not in self.found_words):

                print("found one!!")
                print(current_word)
                self.found_words.append(current_word)
                
                # Optimization: When all words in dictionary are found,   
                # this condition ends the search by returning the path, which
                # sets off a chain of returns back to the base case.  
                if len(self.found_words) is len(self.dictionary):
                    print("Found all the words, returning...")
                    return path
                
        # If a word candidate is not in dictionary...
            return None

        for neighbor in self.next_nodes(path, start_i, start_j):
            i = neighbor[1]
            j = neighbor[2]
            newpath = self.search_from_square(i, j, path, string_path)
            
            # Once the function returns a path (indicating all words have 
            # been found) this condition returns back up the recursive tree, 
            # effectively ending the search
            if newpath: 
                return newpath
            
        # If there are still possible words to find, returning None continues 
        # the backtraking search 
        return None
    
    
    # Adds tiles only if viable based on position, and if not visited before
    ## Extremely verbose, In an interview would you be confined to only N S E W
    ## directions, or would you be expected to impliment a drastically different
    ## method?
    def next_nodes(self, path, i, j):
        
        result = []    
        
        if i > 0:
            node = [self.boggle_board[i-1][j], i-1, j]
            if node not in path:
                result.append(node)
            
        if i < len(self.boggle_board)-1:
            node = [self.boggle_board[i+1][j], i+1, j]
            if node not in path:
                result.append(node)
            
        if j > 0:
            node = [self.boggle_board[i][j-1], i, j-1]
            if node not in path:
                result.append(node)
            
        if j < len(self.boggle_board)-1:
            node = [self.boggle_board[i][j+1], i, j+1]
            if node not in path:
                result.append(node)
            
        if i > 0 and j < len(self.boggle_board)-1:   
             node = [self.boggle_board[i-1][j+1] , i-1 , j+1]
             if node not in path:
                result.append(node)
             
        if i < len(self.boggle_board)-1 and j < len(self.boggle_board)-1:
            node = [self.boggle_board[i+1][j+1], i+1, j+1]
            if node not in path:
                result.append(node)
            
        if i < len(self.boggle_board)-1 and j > 0:
            node = [self.boggle_board[i+1][j-1], i+1, j-1]
            if node not in path:
                result.append(node)
        
        if i > 0 and j > 0:
            node = [self.boggle_board[i-1][j-1], i-1, j-1]
            if node not in path:
                result.append(node)
        else:
            pass

        return result
    
    
def main():
    
    boggle_board = [
    ['G','I','Z'],
    ['U','E','K'],
    ['Q','S','E']
]
   
    n = 4
    dictionary = {"GEEK", "QUIZ", "SEEK", "BENE"}
    
    b = Boggle(boggle_board, n, dictionary)
    
    # Performs dfs on each possible starting square in the list of lists
    # Breaks from the loop early if all words are found
    for start_i in range(len(boggle_board)):
        for start_j in range(len(boggle_board)):
            
            b.search_from_square(start_i, start_j, path=[], string_path=[])

            # breaks out of double loop if already found all words
            if len(b.found_words) is len(b.dictionary):
                print("Returned")
                print(b.found_words)
                break
        else:
            continue     # This logic is rather awkward...
        
        break
          
    if len(b.found_words) is not len(b.dictionary):
        print("Only these words were in the Board: ")
        print(b.found_words)
            
if __name__ == '__main__':
    main()