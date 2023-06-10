# Graphs are composed of 2 separate things: Vertices (Nodes) and Edges (Connections).
# There are no limits to how many other vertices a vertex can connect to.
# Usually, to get from one vertex to the other, you would look at the shortest path. However, edges can be weighted
# This is something that is quite often taken into consideration in Google maps, for example, where paths have "costs"

# Graphs can be categorized into:
# - Directional: Usually an arrow, meaning an edge can only be used to connect two verticies from a single side
# - Bidirectional: Usually a straight line. The connection goes both ways
# - Weighted: A graph in which the edges represent a certain cost to be crossed, which should be optimized at the end.
# - Unweighted: Every edge has the same cost.

# Trees and Linked Lists are also Graphs, only with a limitation of how many child nodes each node can have.

# Graphs use what is called an Adjacency Matrix, a matrix describing the connections between each vertex. 
# The adjacency matrix is usually made up of 0s and 1s, but if there are weights to the edges, we use those instead.
# If a graph is bidirectional, an adjacency matrix will be mirrored/symmetrical to the diagonal line.

# These connections can also be represented with Adjacency Lists. Key -> vertex, Value -> list of neighboring vertices

class Graph:
    def __init__(self) -> None:
        self.adj_list = {} # Using an adjacency list

    def add_vertex(self, vertex) -> bool:
        """Checks if vertex already exists. Otherwise, appends the vertex with an empty list of neighboring vertices"""

        if vertex not in self.adj_list.keys(): # Checks if the vertex is not already in the adjacency list
            self.adj_list[vertex] = [] # Adds the vertex's key:value pair to the adjacency list

            return True # Success
        
        return False # Failure
    
    def add_edge(self, v1, v2) -> bool:
        """Adds a bidirectional edge between two vertices if they exist"""

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():  # Checks if both vertices exist
            self.adj_list[v1].append(v2) # Adds v2 to v1's edge list
            self.adj_list[v2].append(v1) # Adds v1 to v2's edge list

            return True # Success
        
        return False # Failure
    
    def remove_edge(self, v1, v2) -> bool:
        """Removes all connections between both vertices if they exist"""

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # Checking it it exists

            # If they were not previously connected, the exception will be caught
            try: 
                self.adj_list[v1].remove(v2)  # Removes v2 from v1's edge list
                self.adj_list[v2].remove(v1)  # Removes v1 to v2's edge list
            except ValueError:
                pass # Exception ignored

            return True # Success
        
        return False # Failure
    
    def remove_vertex(self, vertex) -> bool:
        """Removes a vertex and all the connections between it and other vertices if it exists"""

        if vertex in self.adj_list.keys(): # Checking if it exists

            # Loops through all of the other vertices that had a connection to the removed vertex
            for other_vertex in self.adj_list[vertex]: 
                self.adj_list[other_vertex].remove(vertex) # Removes the connection

            del self.adj_list[vertex] # Deletes the vertex

            return True # Success 

        return False # Failure

