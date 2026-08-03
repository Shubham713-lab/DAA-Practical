import time
start_time = time.perf_counter()

arr = []


# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)

print(arr)

target  = int(input("Enter target : "))

def binary(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if(arr[mid] == target):
            return mid
        if(arr[mid] > target):
            end = mid - 1
            
        if(arr[mid] < target):
            start = mid + 1

    return -1

pos = binary(arr, target)

print("Element Found at ", pos)

# Time Complexity
print("Time Complexity : ")
print("Best : O(1)")
print("Average : O(log(n))")
print("Worst : O(log(n))")

# Execution Time
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} seconds")
