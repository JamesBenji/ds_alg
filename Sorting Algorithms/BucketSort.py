"""
Bucket sort

"""

def bucket_sort(arr: list[float]) -> list[float]:
    n = len(arr)
    if n <= 1:
        return arr

    buckets = [[] for _ in range(n)]

    for value in arr:
        bucket_index = int(n * value)
        if bucket_index == n:
            bucket_index = n - 1
        buckets[bucket_index].append(value)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(arr))
