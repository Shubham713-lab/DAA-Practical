import time
start_time = time.perf_counter()


arr = []

# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)
print(arr)

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1: return arr

    pivot = arr[len(arr) // 2]

    left = []
    for i in arr:
        if(i < pivot):
            left.append(i)

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(f"Sorted Array : {quick_sort(arr)}")

# Time Complexity
print("Time Complexity : ")
print("Best : O(nlog(n))")
print("Average : O(nlog(n))")
print("Worst : O(n^2)")

# Execution Time
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} seconds")





