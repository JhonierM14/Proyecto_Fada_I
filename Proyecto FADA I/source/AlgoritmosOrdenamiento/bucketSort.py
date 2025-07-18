def insertion_sort_bucket(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(arr):
    if not arr:
        return arr
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        index = int(n * num)
        buckets[index].append(num)
    for i in range(n):
        buckets[i] = insertion_sort_bucket(buckets[i])
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result
