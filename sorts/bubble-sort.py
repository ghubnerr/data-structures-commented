# Bubble sort involves bubbling up the largest item by comparing two terms and swapping them into order

def bubble_sort(my_list):
    # Iterate over the list in reverse order, gradually reducing the unsorted portion
    for i in range(len(my_list) - 1, 0, -1):
        # Iterate over the unsorted portion of the list
        for j in range(i):
            # Compare adjacent elements and swap them if necessary
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]  # Store the current element temporarily
                my_list[j] = my_list[j+1]  # Swap the current element with the next element
                my_list[j+1] = temp  # Assign the temporarily stored element to the next position
    
    return my_list


# Time Complexity: The bubble sort algorithm has Θ(n^2) and O(n^2). This is because it involves two nested loops, resulting in a quadratic time complexity. 
# Space Complexity: Bubble sort is an in-place sorting algorithm, meaning it operates directly on the input list without requiring additional space proportional to the input size. No auxiliary data structures are used, so it is O(1).