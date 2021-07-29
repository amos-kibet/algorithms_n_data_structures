def binary_search(list, element):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid_index = (low + high)#//2
        mid_item = list[mid_index]
        if mid_item == element:
            return mid_index  # why not return guess?? We're returning the index, & not the value
        if mid_item > element:
            high = mid_index - 1
        else:
            low = mid_index + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1))
print(binary_search(my_list, 7))
