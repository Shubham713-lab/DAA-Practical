import time
start_time = time.perf_counter()

arr = []
temp = 0

# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)

print(arr)

for i in range(n):
    for j in range(n-1):
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

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