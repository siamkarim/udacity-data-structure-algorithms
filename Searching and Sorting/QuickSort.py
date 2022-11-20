"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def parts(array, start, end):
    pivot = array[end]
    left = start
    right = end - 1
    yes = True

    while yes:
        while right >= left and array[right] >= pivot:
            right = right - 1
        while array[left] <= pivot and left <= right:
            left = left + 1

        if right < left:
            yes = False
        else:
            m = array[right]
            array[right] = array[left]
            array[left] = m

    m = array[end]
    array[end] = array[left]
    array[left] = m

    return left

def recursive_sort(array, start, end):
    if start < end:
        partition = parts(array, start, end)
        recursive_sort(array, start + 1, end)
        recursive_sort(array, start, end - 1)

def quicksort(array):
    recursive_sort(array, 0, len(array)-1)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))