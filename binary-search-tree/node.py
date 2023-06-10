# Trees can have more than to 2 child nodes. For binary trees, however, there are only left and right children

class Node:
    def __init__(self, value) -> None:
        """Creates a node with no child using the value passed"""
        
        # This is the value that the Node itself will hold.
        self.value = value 

        # This is the pointer to its child Nodes. Both are set to None by default. 
        self.left = None
        self.right = None
