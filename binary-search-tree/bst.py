# Binary Trees have multiple terminologies:
# - Full: All tree nodes have either 0 or 2 child nodes, but not 1. 
# - Perfect: All levels of a tree are thoroughly filled with pairs of sibling Nodes (same parent). It has no gaps.
# - Complete: The tree structure is being filled from left to right, with no gaps in between.

# Binary Search Trees have a Divide and Conquer property: 
# - All nodes below a parent to the right of it are higher in value
# - All nodes below a parent to the left of it are lower in value

# For this reason, any search that occurs in a BST has time complexity of O(log n), meaning it takes log(2) or n time.
# This is because of how the different layers of the tree are structured in levels of 2.

# A Linked List is actually a type of tree with up to only 1 child per Node. In this case, there can be 2 child Nodes.
from node import Node

class BinarySearchTree:
    """Creates an empty BST instance. It does not require any input, as the nodes will be placed in with insert()"""
    def __init__(self) -> None:
        self.root = None # Default

    def insert(self, value):
        """Inserts a Node and maintains the search tree property. Does not accept duplicate values"""
        new_node = Node(value)

        # Check for edge-case: Tree is empty
        if self.root is None:
            self.root = new_node # The root node becomes the value entered
            return True
        
        # Creates a temporary variable that will iterate through child nodes until it finds an empty spot
        temp = self.root # Starts at the root and goes down the tree.

        # While loop will be broken out of with the return statements
        while True:
            
            # Check for wront input: Duplicate value
            if new_node.value == temp.value:
                return False
            
            # Property Maintenance: Compares the value of the new node to the temporary node to decide -- left or right
            elif new_node.value < temp.value: # Smaller value -> Go left

                # Empty spot was found
                if temp.left is None:
                    temp.left = new_node # Places the new node in the tree structure
                    return True
                
                # Empty spot was not found
                else:
                    temp = temp.left # Temporary variable is now its left child, which will be iterated upon next.  
            else: # Higher value -> Go right

                # Empty spot was found
                if temp.right is None:
                    temp.right = new_node # Places the new node in the tree structure
                    return True
                
                # Empty spot was not found
                else:
                    temp = temp.right # Temporary variable is now its right child, which will be iterated upon next.  


    def contains(self, value):
        """Checks if the tree contains a node with a given value. Returns True if so, and False otherwise"""

        # The two lines below are not necessary. If the tree is empty, the loop will not iterate and return False

        # if self.root is None: 
        #     return False

        # Creates a temp variable to point at the current node (or None value) to start from the root down
        temp = self.root

        while temp is not None: # This means: "if the node we're checking out is not empty"

            # Property Maintenance: All to the left is lower, all to the right is higher.
            if value < temp.value: # Goes left if lower
                temp = temp.left
            elif value > temp.value: # Goes right if higher
                temp = temp.right
            else: # Otherwise, this would mean that the node value has matched the value query, so it returns True.
                return True
        
        # If iteration is complete, it means that nothing was found, or else it would have returned True already. 
        return False  