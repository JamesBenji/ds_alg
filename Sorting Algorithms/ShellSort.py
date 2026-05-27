"""
Shell sort

This is an optimization of insertion sort designed to handle larger inputs more effectively by allowing the
exchange of elements that are far apart.
Instead of comparing adjacent elements right away, it starts by comparing elements that are far apart, gradually
reducing the gap between them. By the tme the gap becomes 1, the array is already partially sorted making the final
pass much faster than regular insertion sort.

Complexities
Worst time: O(n^2)
Average time: O(n^1.5)
Best time: O(n log n)

Space: O(1)
"""

input_array = [5,2,3,8]

def shell_sort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp

        gap //= 2

shell_sort(input_array)
print(input_array)