# Implementation of max-heap sort algorithm

def heapify(arr, n, i):
    """Maintain max-heap property for subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current maximum to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore max-heap property
        heapify(arr, i, 0)

    return arr

arr = []

# User Input
n = int(input("Enter size of Array : "))

for i in range(n):
    y = int(input())
    arr.append(y)

print("Original Array : ",arr)

heap_sort(arr)
print("Sorted array : ", arr)