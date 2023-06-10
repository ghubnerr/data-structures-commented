# Stacks are LIFO: Last in, First Out
# They are most often used in browser history, or undo (Cmd + Z), in which you return the last added item.
# The only thing you're supposed to interact with in a Stack is the top-most item.

# Using Linked Lists to create this data structure. The last added item is the head, here, called the top.
# This could also be done with regular lists, using append and pop methods.

from node import Node  

# It's important to structure the Linked List so that the Stack's methods are O(1) and not O(n).
# You can do this by only manipulating the head(top) of the stack. You push to the top, and remove from the top.

class Stack:
    def __init__(self, value) -> None:
        """Creates a Node class instance with the value that is passed and sets it to be the top of the Stack"""
        new_node = Node(value) 

        # Sets the initial node to be the head(top) of the data structure
        self.top = new_node 
        # Length vertically visualized, no difference at all.
        self.height = 1  
    
    def push(self, value) -> None:
        """Creates a Node class instance with the value that is passed, adds to the top of the Stack"""
        new_node = Node(value)

        # Checks for edge-case: Stack is empty
        if self.height == 0: 
            self.top = new_node 
        
        # Otherwise: 
        else:
            new_node.next = self.top # Links the new node to the top-most node
            self.top = new_node # Sets the top pointer to point to the new node

        self.height += 1 # Increases the height for both cases

    def pop(self) -> Node:
        """Pops the top-most Node -- last added -- from the Stack and returns it (if it exists)"""
        
        # Checking for edge-case: Stack is empty
        if self.height == 0:
            return None # Returns none instead of false
        
        # Otherwise: 
        else:
            temp = self.top # Uses a temporary variable to the top-most node
            self.top = self.top.next # Changes top pointer to the successor
            temp.next = None # Removes pointer to old successor 
            self.height -= 1 
            return temp # Returns the popped Node
    


