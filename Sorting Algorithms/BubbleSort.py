"""
Bubble sort

Idea: For each pass, the largest number is pushed towards the end of the list up to its correct position.

Worst-case time complexity is O(n^2).
Best case time complexity is O(n) [with optimization]
Average case time complexity is O(n^2).

Space complexity is O(1) [constant amount of memory is required for length and boolean flag variables]

"""

unsorted_list = [5,8,3,2]

# Since lists are mutable, the algorithm works on the original array passed to it, not on a copy

def bubble_sort(array):
    length = len(array)

    # At the top level, we must make n-1 passes
    # Each pass corresponds to the number of sorted items ie 2nd pass = 2 sorted items
    for i in range(length - 1):
        # in each pass, we loop through the entire array starting from 0 to the decreasing last index
        # since the items at the end are already in their final positions, we do not need to go from 0 to n - 1
        # but rather from 0 to n - 1 - i
        # n - 1 represents the max index; i represents the number of passes which correspond to the number of sorted positions

        # Optimization: Track if a pass has a swap event.
        # The list is already sorted if no swaps happen. This optimization prevents us from making the maximum
        # n - 1 passes even on sorted lists.
        # Without it, the best case scenario of a sorted array would have O(n^2). With the optimization, it is O(n)
        has_a_swap_happened = False

        for j in range(length - 1 - i):
            # compare the number at j with the next number, j + 1
            # if j is bigger than j + 1, swap, otherwise nothing
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                has_a_swap_happened = True

        if not has_a_swap_happened:
            break

bubble_sort(unsorted_list)

print(unsorted_list)