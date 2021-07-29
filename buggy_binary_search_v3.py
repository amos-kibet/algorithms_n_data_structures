import math

def binary_search(sorted_sequence, element):
    mid_index = math.ceil(len(sorted_sequence) / 2)

    while sorted_sequence[mid_index] != element:
        if sorted_sequence[mid_index] > element:
            mid_index = math.ceil(mid_index / 2)

        else:
            mid_index = math.ceil(mid_index + mid_index / 2)

    #return mid_index
    print(mid_index)

sorted_sequence_a = [6, 12, 23, 34, 35, 46]
element_a = 6
binary_search(sorted_sequence_a, element_a)
