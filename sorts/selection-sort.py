def selection_sort(my_list) -> list:
    for i in range(len(my_list) - 1):
        min_index = i  # Assume the current index has the minimum value

        # Find the index of the minimum value in the remaining unsorted part of the list
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j

        if i != min_index:  # If the current index is not the minimum index, swap the elements
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list


# Time complexity: O(n^2). It involves two nested loops: the outer loop runs (n-1) times, and the inner loop runs a decreasing number of times in each iteration.
# Space Complexity: Selection sort is an in-place sorting algorithm, therefore it is O(1).