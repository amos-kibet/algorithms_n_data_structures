def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide; Find the midpoint of the list and divide the sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous steps
    """
    if len(list) == 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoints into sublists
    Returns two sublists, left and right
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list
    :param left:
    :param right:
    :return:
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


a_list = [34, 45, 23, 65, 23, 67, 8, 12, 33]
l = merge_sort(a_list)
print(verify_sorted(a_list))
print(verify_sorted(l))
