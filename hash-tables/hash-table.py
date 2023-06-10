# Hash tables are address bases of key-value pairs, which are run through what's called a Hash Function to be allocated.
# Hash Functions give unique memory addresses for the value that is stored by the key. Python dictionaries work alike.

# They hold two properties:
# - Deterministic: The Hash Function will generate a unique address for every key, even with different values associated
# - One-way: Meaning you can't go from the value to the key, only from the key to the value

# Collisions:
# Given the deterministic property, a Hash Function may generate the same address to different values -> collision.
# Collisions may be sorted through various different ways. Most common are called Separate Chaining and Linear Probing
# - Separate Chaining: Each memory address will be a list that contains all the values assigned to it, sequentially
# - Linear Probing -> Open Addressing: This means that the function will find an empty spot for the value to assign it,
#                                      making the memory addresses hold only one value.

# This Hash Table implements Separate Chaining through lists, but you could use Linked Lists for this purpose as well.

# class Node:
#     def __init__(self, value) -> None:
#         self.value = value
#         self.next = None

class HashTable:
    def __init__(self, size=7) -> None:
        """Creates a data map with given size. Default size = 7"""
        self.data_map = [None] * size


    def __hash(self, key) -> int:   # O(1)
        """Generates a unique hash address for the key. Hash function ensures deterministic property"""
        my_hash = 0 # Initialize hash
        for letter in key: # Loop through the letters in the keys

            # ord(letter) is the ordinal ASCII number for each letter.  
            # 23 is a prime number greater than the data_map's size (indivisibility)        
            # The modulus division will get the hash and return as a remainder from 0 to 6 (given data_map's size = 7)

            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) 

        return my_hash 
    

    def set_item(self, key, value) -> None:   # O(1)
        """Sets the key:value pair relation with a memory address index for the key, storing its value"""
        
        # First, generate the data_map address index for the specific key using the __hash function
        index = self.__hash(key) 

        # Then, check if the index is currently nothing and if so, assign it to hold the value of an empty list
        if self.data_map[index] == None:
            self.data_map[index] = []
        
        # Append the key, value to that specific list in the assigned index of the memory address
        self.data_map[index].append([key, value])


    def get_item(self, key) -> int or None:   # Ω(1) -> Best case, no collisions | O(n) -> Worst case, only collisions
        """Returns the value associated with the key from the data_map. Returns none if key DNE and/or index is None"""

        # Uses the __hash function to find the index pointing to where that key would go -> Deterministic property
        index = self.__hash(key)

        # Checks if the memory address at that index is not empty
        if self.data_map[index] is not None:

            # Then, it loops through all of the lists inside of the list contained in that index of the data map
            for i in range(len(self.data_map[index])):

                # If the key matches the first item in that nested list, it means the value is the following item
                if self.data_map[index][i][0] == key:

                    # Successfully returns the value
                    return self.data_map[index][i][1]
        
        # If any of the conditions are not met, return None
        return None
    

    def keys(self) -> list:  # O(n)
        """Returns all of the keys in the data_map"""

        all_keys = [] # Initializes the list of keys 

        # Loops through all of the memory address indices in the data_map
        for i in range(len(self.data_map)):

            # Checks if that index is not empty
            if self.data_map[i] is not None:

                # Then, loops through all of the nested key:value lists inside of the outer list 
                for j in range(len(self.data_map[i])):

                    # Appends the keys (item in the first index) to the list
                    all_keys.append(self.data_map[i][j][0])
        
        # Finally, returns the list
        return all_keys