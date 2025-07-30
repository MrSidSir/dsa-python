# Topic: Queue + Hash (LRU Cache)
# Real-World Use: Web caching, DB page replacement, OS memory management

from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}              # Stores key-value pairs
        self.queue = deque()         # Maintains access order (most recent at front)
        self.capacity = capacity     # Max capacity of cache

    # GET operation
    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)           # Move the accessed key to front
            self.queue.appendleft(key)
            return self.cache[key]
        return -1                             # If not found

    # PUT operation
    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)           # If exists, remove old position
        elif len(self.cache) == self.capacity:
            old = self.queue.pop()           # Remove least recently used item
            del self.cache[old]

        self.queue.appendleft(key)           # Insert new key at front
        self.cache[key] = value              # Update hashmap

# 🔍 Test Example
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # ✅ Output: 1 (Still in cache)
lru.put(3, 3)      # Evicts key 2 (least recently used)
print(lru.get(2))  # ✅ Output: -1 (Not found)
