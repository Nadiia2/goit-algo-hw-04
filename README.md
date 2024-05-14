# Sorting Algorithms Performance Comparison

This project compares the performance of three sorting algorithms: Merge Sort, Insertion Sort, and Timsort (the built-in Python sorting algorithm). The comparison is based on empirical data obtained by timing the sorting of arrays of different sizes.

## Algorithms

1. **Merge Sort**: A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves.
2. **Insertion Sort**: A simple sorting algorithm that builds the final sorted array one item at a time.
3. **Timsort**: A hybrid sorting algorithm derived from merge sort and insertion sort. It is used as the default sorting algorithm in Python.

## Results

The following table shows the execution time (in seconds) for sorting arrays of different sizes using each algorithm.

| Size   | Merge Sort | Insertion Sort | Timsort  |
| ------ | ---------- | -------------- | -------- |
| 1000   | 0.001781   | 0.021006       | 0.000081 |
| 10000  | 0.023626   | 2.532113       | 0.000990 |
| 100000 | 0.350864   | 274.013307     | 0.010771 |

## Conclusion

The empirical data confirms the theoretical time complexities of the sorting algorithms:

- **Merge Sort** has a time complexity of O(n log n) and performs consistently well on large datasets.
- **Insertion Sort** has a time complexity of O(n^2), making it inefficient for large datasets but relatively efficient for small ones.
- **Timsort** combines the advantages of merge sort and insertion sort, making it extremely efficient with a time complexity of O(n log n) and additional optimizations for real-world data.

These results demonstrate why Timsort is the preferred sorting algorithm in Python: it offers a balance of efficiency and performance for a wide range of input data sizes and patterns.
