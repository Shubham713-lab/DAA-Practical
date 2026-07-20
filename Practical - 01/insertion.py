import time
start_time = time.perf_counter()

arr = []

# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)
print(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while((j >= 0 )& (arr[j] > key)):
        arr[j + 1] = arr[j]
        j = j-1
    arr[j + 1] = key

print(f"Sorted Array : {arr}")

# Time Complexity
print("Time Complexity : ")
print("Best : O(n)")
print("Average : O(n^2)")
print("Worst : O(n^2)")

# Execution Time
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} seconds")