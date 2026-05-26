"""
Selection sort

Idea: Select the smallest number from the unsorted portion of the array and place it in its correct position.

Selection sort is a comparison-based sorting algorithm
                    that works by repeatedly finding the minimum element
                    from the unsorted portion of the array
                    and
                    placing it at the beginning of the unsorted portion.

At any point during the algorithm, the array is split into two sides:
    Sorted "left" side [elements in final position]
    Unsorted "right" side [elements to be processed]

In each pass, the algorithm selects the smallest element in the unsorted region and swaps it for the first element
in the unsorted region.

Complexities:
Best case: O(n^2)
Average case: O(n^2)
Worst case: O(n^2)

Space: O(1)

Number of swaps: O(n), better than Bubble sort's O(n^2)
Stable: No [swapping can change the relative order of equal elements)
Adaptive: No [Major][Does not benefit from partially sorted input since it always does the same number of comparisons]
          Bubble sort allows for early termination when no swaps occur

"""

input_array = [5,8,2,3]

def selection_sort(array):
    n = len(array)

    # length - 1 represents the number of passes to be made (n - 1)
    for i in range(n - 1):
        smallest_index = i

        for j in range(i + 1, n):
            if array[j] < array[smallest_index]:
                smallest_index = j

        # swap only when a smaller number was actually found by index
        # this prevents dead swaps when i = smallest index
        if i != smallest_index:
            array[i], array[smallest_index] = array[smallest_index], array[i]

selection_sort(input_array)

print(input_array)