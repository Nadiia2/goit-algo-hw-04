import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def tim_sort(arr):
    arr.sort()

def main():
    results = []
    sizes = [1000, 10000, 100000]

    for size in sizes:
        data = [random.randint(0, 1000) for _ in range(size)]
        
        merge_time = timeit.timeit(
            stmt='merge_sort(data)',
            setup=f'data = {data}; from __main__ import merge_sort',
            number=1
        )
        insertion_time = timeit.timeit(
            stmt='insertion_sort(data)',
            setup=f'data = {data}; from __main__ import insertion_sort',
            number=1
        )
        tim_sort_time = timeit.timeit(
            stmt='tim_sort(data)',
            setup=f'data = {data}; from __main__ import tim_sort',
            number=1
        )

        results.append((size, merge_time, insertion_time, tim_sort_time))

    print("Size\tMerge Sort\tInsertion Sort\tTimsort")
    for size, merge_time, insertion_time, tim_sort_time in results:
        print(f"{size}\t{merge_time:.6f}\t{insertion_time:.6f}\t{tim_sort_time:.6f}")

if __name__ == "__main__":
    main()
