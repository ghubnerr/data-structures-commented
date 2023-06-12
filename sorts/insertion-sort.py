# Insertion sort is really good for almost sorted data -> O(n) instead of O(n^2)

def insertion_sort(my_list):
    # Iterate over the list starting from the second element
    for i in range(1, len(my_list)):
        temp = my_list[i]  # Store the current element temporarily
        j = i - 1  # Set the index of the previous element
        
        # Compare the current element with the elements before it and shift them to the right if necessary
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]  # Shift the element to the right
            my_list[j] = temp  # Insert the current element in its correct position
            j -= 1  # Move to the previous element
        
    return my_list


# Time Complexity: Insertion sort is Θ(n^2) and O(n^2), but Ω(n). This is because, in the worst case, for each element, it may need to be compared and shifted to the leftmost position in the sorted portion of the list
# Space Complexity: Insertion sort is an in-place sorting algorithm, meaning it operates directly on the input list without requiring additional space proportional to the input size. Therefore, it's O(1).