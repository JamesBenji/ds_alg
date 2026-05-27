"""
Insertion sort
It builds a sorted array one element at a time. It picks the next unsorted element and inserts it into its correct position
within the already-sorted region of the array.

It relies on "element shifts and duplicate rewriting" to build a sorted array. Regardless of the unsorted element it takes in on the next
iteration, it will place it in the correct relative position within the sorted region of the array.

At any point during the algorithm, the array is divided into two regions:
    - Sorted "left" side
    - Unsorted "right" side

The algorithm repeatedly takes the first element from the unsorted region and places it where it belongs in the sorted
region shifting larger elements to the right to make room. Pretty intuitive :)

It is valuable in scenarios where data is nearly sorted or arriving in a stream.
"""

input_list = [5,3,2,8]

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):

        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

insertion_sort(input_list)

print(input_list)