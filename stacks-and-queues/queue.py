# Queues are FIFO: First in, First Out
# They are like lines, in which the first person to get to the line is the first one to exit it.
# Here, we use methods called enqueue and dequeue to add/remove from the queue.
# Like with stacks, the only thing you interact with in queue is the first-most item.

# Using Linked List to create this Data Structure
from node import Node

# It's important to structure the Linked List so that the Queue's methods are O(1) and not O(n).
# You can do this by enqueueing from the last node -> O(1), and dequeueing from the first node -> O(1)

class Queue:
    def __init__(self, value) -> None:
        """Creates a Node class instance with the value that is passed and sets it to be the front  of the Queue"""
        new_node = Node(value)

        # Sets the initial node to be the first and the last node of the Queue (since it's the only one)
        self.first = new_node 
        self.last = new_node

        self.length = 1
    
    def enqueue(self, value) -> None:
        """Creates a Node class instance with the value that is passed, adds to the back of the Queue"""
        new_node = Node(value)

        # Checking for edge-case: Queue is empty
        if self.first is None:
            self.first = new_node
            self.last = new_node
        
        # Otherwise: 
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1 # Increase length for both cases

    def dequeue(self) -> Node:
        """Removes the first Node -- first added -- from the Queue and returns it (if it exists)"""

        # Checking for edge-case: Queue is empty
        if self.first is None:
            return None # Returns none instead of false
        
        temp = self.first # Use a variable to point to the front node

        # Checking for edge-case: Queue only has one item
        if self.first == self.last:
            self.first = None # Remove pointers to Node
            self.last = None 

        # Otherwise: 
        else:
            self.first = self.first.next # Point to the next node on the queue to be the first
            temp.next = None # Remove pointer from dequeued node.

        self.length -= 1 # Decrease length for the last two cases
        
        return temp


