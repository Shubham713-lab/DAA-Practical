# Implementation and Time Analysis of Linear Search and Binary Search Algorithms

## Project Overview
This project implements two fundamental searching algorithms: **Linear Search** and **Binary Search**. It compares their working principles, implementation, and execution time to evaluate their efficiency under different conditions. The project also analyzes the time complexity of both algorithms to determine their suitability for various applications.

## Objectives
- Implement Linear Search and Binary Search algorithms.
- Compare the performance of both algorithms.
- Analyze their best, average, and worst-case time complexities.
- Understand the advantages and limitations of each algorithm.

## Algorithms

### Linear Search
Linear Search examines each element in the array one by one until the target element is found or the end of the array is reached.

**Characteristics:**
- Works with both sorted and unsorted arrays.
- Simple and easy to implement.
- Suitable for small datasets.

### Binary Search
Binary Search repeatedly divides a **sorted** array into two halves to locate the target element efficiently.

**Characteristics:**
- Requires the array to be sorted.
- Significantly faster for large datasets.
- Uses the divide-and-conquer approach.

## Time Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

## Overall Summary
This project demonstrates the implementation and comparative analysis of Linear Search and Binary Search algorithms. Linear Search performs a sequential search and is suitable for unsorted or small datasets, whereas Binary Search provides faster searching by repeatedly dividing a sorted array into halves. The performance comparison shows that Binary Search is considerably more efficient than Linear Search for large sorted datasets because of its logarithmic time complexity.

## Conclusion
The study concludes that both searching algorithms have their own advantages depending on the application. Linear Search is simple, requires no preprocessing, and works on any dataset, making it suitable for small or unsorted collections. Binary Search is highly efficient for large datasets but requires the data to be sorted before searching. Therefore, Binary Search is the preferred choice whenever the data is sorted, while Linear Search remains a practical solution for smaller or unsorted datasets.

## References
1. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms*, MIT Press.
2. Robert Sedgewick and Kevin Wayne, *Algorithms*, Addison-Wesley.
3. Donald E. Knuth, *The Art of Computer Programming, Volume 3: Sorting and Searching*.