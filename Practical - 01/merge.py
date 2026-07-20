
import time
start_time = time.perf_counter()

arr = []

# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)
print(arr)

def merge_sort(arr):
    # Base case: A list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. Conquer: Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # 3. Combine: Merge the two sorted halves back into the original array
    i = j = k = 0

    # Compare elements from left and right halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Check if any elements were left over in the left half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Check if any elements were left over in the right half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

print(f"Sorted Array : {merge_sort(arr)}")

# Time Complexity
print("Time Complexity : ")
print("Best : O(nlogn)")
print("Average : O(n^2)")
print("Worst : O(n^2)")

# Execution Time
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} seconds")

# Tn = 2Tn(n/2) + n



