"""
Counting sort

"""

input_array = [5,2,3,8]

def counting_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size
    for val in arr:
        count[val - min_val] += 1

    for i in range(1, range_size):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        idx = count[arr[i] - min_val] - 1
        output[idx] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

sorted_array = counting_sort(input_array)
print(sorted_array)