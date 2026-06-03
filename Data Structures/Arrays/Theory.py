"""
Array theory:

An array is a data structure used to store a collection of elements of the same type, arranged in a contiguous block
of memory. This is a requirement in order to support the superfast access of elements by index in constant time
using the formula:

    Address of array[i] = Base address + (i * element size)

Array operations include:
    1. Accessing by index
    2. Traversal via iteration
    3. Insertion
    4. Deletion
    5. Search

Common array patterns (to be explained in following sections):
    1. Two pointer technique [traversing an array from both ends]
    2. Sliding window
    3. Prefix sum
    4. Dynamic programming

"""