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
    
#----------------------------------------------------------------------------------------------------------------------#

    # Recursive Binary Search Tree

    def __r_contains(self, current_node, value) -> bool:
        """Recursive method not called directly. Use r_contains(value) instead"""
        
        # Base cases -> If node is empty or if the value is found, the recursion is broken.
        if current_node == None:
            return False 
        if value == current_node.value:
            return True
        
        # Recursive case -> Goes down a node by comparing the target value to the current node
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) # Going left
        
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value) # Going right
        

    def r_contains(self, value) -> bool:
        """Returns true if tree contains value. False otherwise"""

        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value):
        """Recursive method not called directly. Use r_insert(value) instead"""
        
        # This means that we've found an empty spot to create our Node at
        if current_node == None:
            return Node(value)
        
        # Recursive case -> Points down a node by comparing the target value to the current node
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value) # Pointing left
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) # Pointing right

        # Note that the recursive assignment happens to the pointers of the current node.


    def r_insert(self, value) -> None:
        """Inserts node in the tree"""

        # Checking for edge-case: Tree is empty
        if self.root == None:
            self.root = Node(value)

        # Otherwise, pass it into a recursive function that starts at the root to insert it
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        """Finds the minimal value of a subtree (or the whole tree)"""

        while current_node.left is not None: # Min value -> Left-most child
            current_node = current_node.left

        return current_node.value # Returns value

    def __delete_node(self, current_node, value):
        """Recursive method not called directly. Use delete_node(value) instead"""

        # Base case: Node is not found and traversal reached a leaf
        if current_node == None:
            return None
        
        # Recursive cases: Points down to the node according to its value relative to the target value
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value) # Points left
        elif value > current_node.value:
                    current_node.right = self.__delete_node(current_node.right, value) # Points right

        # Node found -> Delete 
        else:
            # Case I: Removing a leaf node
            if current_node.left == None and current_node.right == None:
                return None # This will make the parent node no longer point to it

            # Case II: Removing a node that has a child on the right, but not the left
            elif current_node.left == None:
                current_node = current_node.right # Changes parent's pointer to the grandchild

            # Case III: Removing a node that has a child on the left, but not the right
            elif current_node.right == None:
                current_node = current_node.left # Changes parent's pointer to the grandchild

            # Case IV: Removing a node that has both a child on the left, and on the right -> Uses helper method
            else:
                # "Replaces" the node to be removed with the nearest highest value to it (left-most child to the right)
                sub_tree_min_value = self.min_value(current_node.right)
                current_node.value = sub_tree_min_value
                
                # Then, traverses the tree to delete the duplicate value
                current_node.right = self.__delete_node(current_node, sub_tree_min_value)

        return current_node


    def delete_node(self, value) -> None:
        """Removes pointers pointing to the Node containing target value. Rearranges tree accordingly"""

        self.__delete_node(self.root, value)

    def invert(self) -> None:
        """Calls on helper recursive function"""

        self.__invert(self.root)
        return True

    def __invert(self, current_node) -> Node:
        """Recursive function. Inverts left child with right child through simultaneous reassingment"""

        # Base Case
        if current_node == None:
            return None
        
        # Simultaneous Reassignment (No need for temporary variable)
        else:
            current_node.right, current_node.left = self.__invert(current_node.left), self.__invert(current_node.right)
        
        # Return node for pointer
        return current_node

# ---------------------------------------------------------------------------- #
    
    # Tree traversal

    # Breadth-First Search
    # BFS is a graph traversal algorithm that explores a graph or a tree structure level by level. 
    # It starts at a specified node (often the root node) and systematically explores all the neighboring nodes at the current level before moving on to the next level.
    # BFS ensures that all nodes at a particular depth or level are visited before moving on to nodes at the next depth.
    # BFS explores the tree level by level, visiting the nodes from left to right within each level.

    # Sample Tree Structure:
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7

    # bfs() return: [1, 2, 3, 4, 5, 6, 7]


    def bfs(self) -> list:
        """Breadth-First Search Traversal. Returns Hierarchical Order (Levels)"""

        current_node = self.root  # Start at the root node
        queue = []  # Initialize an empty queue (also called frontier)
        results = []  # Initialize an empty list to store the results
        queue.append(current_node)  # Add the current node to the queue

        while len(queue) > 0:  # Continue until the queue is empty
            current_node = queue.pop(0)  # Remove and retrieve the first node from the queue
            results.append(current_node.value)  # Add the value of the current node to the results

            if current_node.left is not None:  # If the current node has a left child
                queue.append(current_node.left)  # Add the left child to the queue

            if current_node.right is not None:  # If the current node has a right child
                queue.append(current_node.right)  # Add the right child to the queue

        return results 

    # Depth-First Search
    # DFS is a graph traversal algorithm that explores a graph or a tree structure in a depth-first manner.
    # DFS explores the tree by going as deep as possible before exploring sibling nodes, and it can do so in three different manners.

    # Sample Tree Structure:
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7

    # dfs_pre_order() return: [1, 2, 4, 5, 3, 6, 7]
    # dfs_in_order() return: [4, 2, 5, 1, 6, 3, 7]
    # dfs_post_order() return: [4, 5, 2, 6, 7, 3, 1]
    

def dfs_pre_order(self) -> list:
    """Depth-First Search PreOrder Traversal"""

    results = []
    
    def traverse(current_node):
        """Recursive function that performs pre-order traversal"""

        results.append(current_node.value)  # Append current node value to results BEFORE traversing children
        
        if current_node.left is not None:  # Traverse left child first, if it's not empty
            traverse(current_node.left)
        
        if current_node.right is not None:  # Traverse right child next, if it's not empty
            traverse(current_node.right)
    
    traverse(self.root)  # Start traversal from the root

    return results


def dfs_in_order(self) -> list:
    """Depth-First Search InOrder Traversal"""

    results = []
    
    def traverse(current_node):
        """Recursive function that performs in-order traversal"""

        if current_node.left is not None:  # Traverse left child first, if it's not empty
            traverse(current_node.left)
        
        results.append(current_node.value)  # Append current value to results IN-BETWEEN traversing children
        
        if current_node.right is not None:  # Traverse right child next, if it's not empty
            traverse(current_node.right)
    
    traverse(self.root)  # Start traversal from the root

    return results


def dfs_post_order(self) -> list:
    """Depth-First Search PostOrder Traversal"""

    results = []
    
    def traverse(current_node):
        """Recursive function that performs post-order traversal"""

        if current_node.left is not None:  # Traverse left child first, if it's not empty
            traverse(current_node.left)
        
        if current_node.right is not None:  # Traverse right child next, if it's not empty
            traverse(current_node.right)
        
        results.append(current_node.value)  # Append current value to results AFTER traversing children
    
    traverse(self.root)  # Start traversal from the root

    return results
