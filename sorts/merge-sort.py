# Merge sort is a sorting algorithm that uses a divide-and-conquer approach. It repeatedly divides the input list into smaller halves until they are single elements or empty.
# Then, it merges the sorted halves back together, comparing and arranging the elements to obtain the final sorted result. 
# It handles larger lists by recursively splitting and merging, resulting in a sorted list in ascending order.

# Helper function
def merge(list1, list2) -> list:  # Merge two lists in sorted order
    combined_list = []  # Resultant merged list
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2
    
    # Iterate through both lists and compare elements to merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])  # Append the smaller element from list1
            i += 1
        else:
            combined_list.append(list2[j])  # Append the smaller element from list2
            j += 1
    
    # Append any remaining elements from list1
    while i < len(list1):
        combined_list.append(list1[i])
        i += 1
    
    # Append any remaining elements from list2
    while j < len(list2):
        combined_list.append(list2[j])
        j += 1
    
    return combined_list

# Recursive function
def merge_sort(my_list) -> list:  # Perform merge sort on the list
    if len(my_list) == 1:  # Base case: list with a single element is already sorted
        return my_list
    
    mid_index = int(len(my_list) / 2)  # Find the midpoint of the list
    left = merge_sort(my_list[:mid_index])  # Recursively sort the left half of the list
    right = merge_sort(my_list[mid_index:])  # Recursively sort the right half of the list
    
    return merge(left, right)  # Merge the sorted left and right halves


# Time Complexity: Merge sort is O(n log n). The merging step is O(n) since it compares and merges each element from the two halves. The comparison is log n along recursion, resulting in the overall time complexity of O(n log n).
# Space Complexity: O(n), because it requires additional space to store the merged lists during the merging process.

