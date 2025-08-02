import heapq

def kthSmallest(arr, k):
    # Step 1: Convert the array into a Min Heap
    heapq.heapify(arr)

    # Step 2: Remove the smallest (k-1) elements
    for _ in range(k - 1):
        heapq.heappop(arr)

    # Step 3: The next element is the k-th smallest
    return heapq.heappop(arr)

# -------------------------------
# 🔁 Test the function
arr = [7, 10, 4, 3, 20, 15]
k = 3

result = kthSmallest(arr, k)
print(f"The {k}-th smallest element is: {result}")
