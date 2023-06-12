# Quicksort is a widely used sorting algorithm based on the divide-and-conquer principle. 
# It works by selecting a pivot element from the list and partitioning the other elements into two sublists, according to whether they are less than or greater than the pivot. 
# This process is recursively applied to the sublists until the entire list is sorted.

# Helper Function
def swap(my_list, index1, index2) -> None:  # In-place swap of elements in a list
    temp = my_list[index1]  # Store the element at index1 temporarily
    my_list[index1] = my_list[index2]  # Assign the element at index2 to index1
    my_list[index2] = temp  # Assign the stored element to index2


# Helper Function
def pivot(my_list, pivot_index, end_index) -> int:  # Partition the list around a pivot element
    swap_index = pivot_index  # Initialize the swap index to the pivot index
    
    # Iterate through the elements from pivot_index + 1 to end_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:  # Compare the element with the pivot
            swap_index += 1  # Increment the swap index
            swap(my_list, swap_index, i)  # Swap the element with the swap index
    
    swap(my_list, pivot_index, swap_index)  # Swap the pivot element with the swap index
    return swap_index  # Return the final index of the pivot element after partitioning


# Quick Sort
def quick_sort_helper(my_list, left, right) -> list:  # Helper function for the quick sort algorithm
    if left < right:
        pivot_index = pivot(my_list, left, right)  # Select a pivot and partition the list
        quick_sort_helper(my_list, left, pivot_index - 1)  # Recursively sort the left partition
        quick_sort_helper(my_list, pivot_index + 1, right)  # Recursively sort the right partition
    return my_list  # Return the sorted list


# Enters the indexes on its own and calls Quick Sort
def quick_sort(my_list) -> list:  # Perform quick sort on the list
    return quick_sort_helper(my_list, 0, len(my_list) - 1)  # Call the helper function with initial indices


# Time complexities: Θ(n log n), Ω(n log n), O(n^2) -> Almost-sorted data: Worst Case
# Space complexity: It has an in-place space complexity of O(log n) for the recursive call stack.