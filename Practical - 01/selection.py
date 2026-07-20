import time
start_time = time.perf_counter()

arr = []

# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)
print(arr)


for i in range(n - 1):
    min = i
    for j in range(i+1, n):
        if(arr[j] < arr[min]):
            min = j

    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

print(f"Sorted Array : {arr}")

# Time Complexity
print("Time Complexity : ")
print("Best : O(nlogn)")
print("Average : O(nlogn)")
print("Worst : O(nlogn)")

# Execution Time
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} seconds")

# (n*(n-1))/2