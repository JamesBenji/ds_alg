"""
Radix sort

"""

def radix_sort(arr):
    if len(arr) <= 1:
        return arr

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)
