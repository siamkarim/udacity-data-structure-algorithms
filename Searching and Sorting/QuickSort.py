"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) != 1:
        n = len(array)
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                small = array[i + 1]
                big = array[i]
                array[i] = small
                array[i + 1] = big
    return array



test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
print(quicksort(test))
print(quicksort(test))
print(quicksort(test))