# 1. Insert at end
arr = [1,2,3]
arr.append(4)
print(arr)

# 2. Insert at specific position
arr.insert(1, 10)
print(arr)

# 3. Delete by value
arr.remove(10)
print(arr)

# 4. Delete by index
del arr[0]
print(arr)

# 5. Stack using list
stack = []
stack.append(1)
stack.append(2)
print("Pop:", stack.pop())

# 6. Queue using list
queue = []
queue.append(1)
queue.append(2)
print("Dequeue:", queue.pop(0))

# 7. Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = self.rear = -1
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if self.front == -1:
            print("Queue Empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
print(cq.dequeue())

# 8. Reverse linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
# (create linked list and call reverse as needed)

# 9. Detect loop
def detectLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 10. Merge two sorted arrays
arr1 = [1,3,5]
arr2 = [2,4,6]
i=j=0
res=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        res.append(arr1[i])
        i+=1
    else:
        res.append(arr2[j])
        j+=1
res+=arr1[i:]
res+=arr2[j:]
print(res)

# 11. Linear search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
print(linear_search([1,2,3],2))

# 12. Binary search
def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l<=r:
        m = (l+r)//2
        if arr[m]==x:
            return m
        elif arr[m]<x:
            l = m+1
        else:
            r = m-1
    return -1
print(binary_search([1,2,3,4,5],4))

# 13. Find missing number
arr = [1,2,4,5]
n = 5
total = n*(n+1)//2
print("Missing:", total - sum(arr))

# 14. Find duplicates
arr = [1,2,3,2,1]
seen = set()
dup = set()
for i in arr:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print("Duplicates:", dup)

# 15. Insertion sort
arr = [5,2,9,1]
for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key
print("Sorted:", arr)


# [1, 2, 3, 4]
# [1, 10, 2, 3, 4]
# [1, 2, 3, 4]
# [2, 3, 4]
# Pop: 2
# Dequeue: 1
# 1
# [1, 2, 3, 4, 5, 6]
# 1
# 3
# Missing: 3
# Duplicates: {1, 2}
# Sorted: [1, 2, 5, 9]