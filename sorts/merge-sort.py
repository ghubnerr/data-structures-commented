# Does not occur in place
# Space complexity: O(n)
# Time complexity: O(n log n)

# Helper function
def merge(list1, list2) -> list: # O(n)
    combined_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1

    while i < len(list1):
        combined_list.append(list[i])
        i += 1

    while j < len(list2):
        combined_list.append(list2[j])
        j += 1

    return combined_list

# Recursive function
def merge_sort(my_list) -> list: # O (log n)
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)
