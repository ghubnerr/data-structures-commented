# Bubble sort involves bubbling up the largest item by comparing two terms and swapping them into order

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

original_list = [1,23,57,85,2,2,3,7]

bubble_sort(original_list)

print(original_list)