"""
Merge sort

It is a divide-and-conquer algorithm. It breaks a problems into smaller subproblems, solves each one independently,
and then combines the results.

How it works:
1. If the array has 0 or 1 elements, return [base case]
2. Find the midpoint: mid = left + (right + left) / 2
3. Recursively sort the left half: mergeSort(arr, left, mid)
4. Recursively sort the right half: mergeSort(arr, mid + 1, right)
5. Merge the two sorted halves back into the original array
"""

input_array = [5,2,3,8]

def merge_sort(array, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)
    merge(array, left, mid, right)

def merge(arr, left, mid, right):
    # the range is [left, mid + 1) Upper limit exclusive
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1: right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        j += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        i += 1
        j += 1

n = len(input_array)
merge_sort(input_array, 0, n)
print(input_array)
