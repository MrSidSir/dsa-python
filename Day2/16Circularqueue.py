class CircularQueue:
    def __init__(self, k):
        self.q = [None] * k  # Fixed: [Node]*k -> [None]*k
        self.size = k
        self.front = self.rear = -1
    
    def enqueue(self, value):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            return "Full"
        
        # If queue is empty, set front to 0
        if self.front == -1:
            self.front = 0
        
        # Move rear pointer and add value
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value  # Fixed: Value -> value
        return f"Enqueued: {value}"
    
    def dequeue(self):
        # Check if queue is empty
        if self.front == -1:
            return "Empty"
        
        # Get the value to return
        value = self.q[self.front]
        
        # If only one element, reset pointers
        if self.front == self.rear:
            self.front = self.rear = -1  # Fixed: fronnt -> front
        else:
            # Move front pointer
            self.front = (self.front + 1) % self.size
        
        return f"Dequeued: {value}"
    
    def display(self):
        if self.front == -1:
            return "Queue is empty"
        
        elements = []
        i = self.front
        while True:
            elements.append(str(self.q[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.size
        
        return "Queue: [" + ", ".join(elements) + "]"

# Test the implementation
cq = CircularQueue(3)
print(cq.enqueue(1))    # Enqueued: 1
print(cq.enqueue(2))    # Enqueued: 2  
print(cq.enqueue(3))    # Enqueued: 3
print(cq.enqueue(4))    # Full
print(cq.display())     # Queue: [1, 2, 3]

print(cq.dequeue())     # Dequeued: 1
print(cq.display())     # Queue: [2, 3]
print(cq.enqueue(4))    # Enqueued: 4
print(cq.display())     # Queue: [2, 3, 4]

# larqueue.py
# Enqueued: 1
# Enqueued: 2
# Enqueued: 3
# Full
# Queue: [1, 2, 3]
# Dequeued: 1
# Queue: [2, 3]
# Enqueued: 4
# Queue: [2, 3, 4]