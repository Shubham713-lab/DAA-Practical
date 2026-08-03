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

def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

pos = linear(arr, target)

print("Element Found at ", pos)

# Time Complexity
print("Time Complexity : ")
print("Best : O(1)")
print("Average : O(n)")
print("Worst : O(n)")

# Execution Time
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} seconds")
