from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):  # Fixed: __init__ instead of _init_
        self.cache = OrderedDict()
        self.cap = capacity
    
    def get(self, key):
        if key in self.cache:
            # Move to end (mark as recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):  # Fixed: proper indentation
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Add new key-value pair
            if len(self.cache) >= self.cap:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
        
        self.cache[key] = value  # Fixed: 'value' instead of 'Value'

# 🔄 **WORKFLOW DEMONSTRATION**
print("=== LRU Cache Workflow Demo ===")
lru = LRUCache(2)

print("\n1️⃣ Initial Setup: Cache capacity = 2")
print(f"Cache state: {dict(lru.cache)}")

print("\n2️⃣ Adding first item: put(1, 'Page1')")
lru.put(1, 'Page1')
print(f"Cache state: {dict(lru.cache)}")

print("\n3️⃣ Adding second item: put(2, 'Page2')")
lru.put(2, 'Page2')
print(f"Cache state: {dict(lru.cache)}")

print("\n4️⃣ Accessing key 1: get(1)")
result = lru.get(1)
print(f"Retrieved: {result}")
print(f"Cache state after access: {dict(lru.cache)} (key 1 moved to end)")

print("\n5️⃣ Adding third item (capacity exceeded): put(3, 'Page3')")
lru.put(3, 'Page3')
print(f"Cache state: {dict(lru.cache)} (key 2 evicted - was least recently used)")

print("\n6️⃣ Trying to access evicted key 2: get(2)")
result = lru.get(2)
print(f"Retrieved: {result} (not found)")

print("\n7️⃣ Adding fourth item: put(4, 'Page4')")
lru.put(4, 'Page4')
print(f"Cache state: {dict(lru.cache)} (key 1 evicted)")

print("\n8️⃣ Final access tests:")
print(f"get(1): {lru.get(1)} (evicted)")
print(f"get(3): {lru.get(3)} (available)")
print(f"get(4): {lru.get(4)} (available)")
print(f"Final cache state: {dict(lru.cache)}")

print("\n" + "="*50)
print("🌍 **REAL-WORLD APPLICATIONS**")
print("="*50)

print("""
1️⃣ **Web Browser Cache**
   - Stores recently visited web pages
   - Evicts oldest pages when memory limit reached
   - Faster loading of frequently visited sites

2️⃣ **Database Query Cache**
   - Caches query results in memory
   - Avoids expensive database lookups
   - Used in MySQL, PostgreSQL, Redis

3️⃣ **CPU Cache**
   - L1, L2, L3 caches in processors
   - Stores frequently accessed memory data
   - Hardware implementation of LRU

4️⃣ **Operating System Page Replacement**
   - Virtual memory management
   - Decides which pages to swap to disk
   - Linux kernel uses LRU approximation

5️⃣ **CDN (Content Delivery Networks)**
   - Caches popular content closer to users
   - Evicts less popular content
   - Used by CloudFlare, AWS CloudFront

6️⃣ **Mobile App Memory Management**
   - Caches images, data in mobile apps
   - Prevents out-of-memory errors
   - Instagram, Facebook use LRU caching

7️⃣ **Compiler Optimizations**
   - Register allocation in compilers
   - Caches frequently used variables
   - GCC, LLVM use LRU algorithms
""")

print("\n" + "="*50)
print("⚡ **PERFORMANCE BENEFITS**")
print("="*50)
print("""
✅ Time Complexity: O(1) for both get() and put()
✅ Space Complexity: O(capacity)
✅ OrderedDict provides efficient operations:
   - Insertion/Deletion: O(1)
   - Move to end: O(1)
   - Access: O(1)
""")

print("\n" + "="*50)
print("🔧 **CODE FIXES APPLIED**")
print("="*50)
print("""
❌ Original Issues:
   - _init_ → __init__ (constructor syntax)
   - Wrong indentation in put() method
   - 'Value' → 'value' (variable name typo)

✅ Fixed Version:
   - Proper constructor: __init__
   - Correct indentation and logic flow
   - Fixed variable names and syntax
""")


# === LRU Cache Workflow Demo ===

# 1️⃣ Initial Setup: Cache capacity = 2
# Cache state: {}

# 2️⃣ Adding first item: put(1, 'Page1')
# Cache state: {1: 'Page1'}

# 3️⃣ Adding second item: put(2, 'Page2')
# Cache state: {1: 'Page1', 2: 'Page2'}

# 4️⃣ Accessing key 1: get(1)
# Retrieved: Page1
# Cache state after access: {2: 'Page2', 1: 'Page1'} (key 1 moved to end)

# 5️⃣ Adding third item (capacity exceeded): put(3, 'Page3')
# Cache state: {1: 'Page1', 3: 'Page3'} (key 2 evicted - was least recently used)

# 6️⃣ Trying to access evicted key 2: get(2)
# Retrieved: -1 (not found)

# 7️⃣ Adding fourth item: put(4, 'Page4')
# Cache state: {3: 'Page3', 4: 'Page4'} (key 1 evicted)

# 8️⃣ Final access tests:
# get(1): -1 (evicted)
# get(3): Page3 (available)
# get(4): Page4 (available)
# Final cache state: {3: 'Page3', 4: 'Page4'}

# ==================================================
# 🌍 **REAL-WORLD APPLICATIONS**
# ==================================================

# 1️⃣ **Web Browser Cache**
#    - Stores recently visited web pages
#    - Evicts oldest pages when memory limit reached
#    - Faster loading of frequently visited sites

# 2️⃣ **Database Query Cache**
#    - Caches query results in memory
#    - Avoids expensive database lookups
#    - Used in MySQL, PostgreSQL, Redis

# 3️⃣ **CPU Cache**
#    - L1, L2, L3 caches in processors
#    - Stores frequently accessed memory data
#    - Hardware implementation of LRU

# 4️⃣ **Operating System Page Replacement**
#    - Virtual memory management
#    - Decides which pages to swap to disk
#    - Linux kernel uses LRU approximation

# 5️⃣ **CDN (Content Delivery Networks)**
#    - Caches popular content closer to users
#    - Evicts less popular content
#    - Used by CloudFlare, AWS CloudFront

# 6️⃣ **Mobile App Memory Management**
#    - Caches images, data in mobile apps
#    - Prevents out-of-memory errors
#    - Instagram, Facebook use LRU caching

# 7️⃣ **Compiler Optimizations**
#    - Register allocation in compilers
#    - Caches frequently used variables
#    - GCC, LLVM use LRU algorithms


# ==================================================
# ⚡ **PERFORMANCE BENEFITS**
# ==================================================

# ✅ Time Complexity: O(1) for both get() and put()
# ✅ Space Complexity: O(capacity)
# ✅ OrderedDict provides efficient operations:
#    - Insertion/Deletion: O(1)
#    - Move to end: O(1)
#    - Access: O(1)


# ==================================================
# 🔧 **CODE FIXES APPLIED**
# ==================================================

# ❌ Original Issues:
#    - _init_ → __init__ (constructor syntax)
#    - Wrong indentation in put() method
#    - 'Value' → 'value' (variable name typo)

# ✅ Fixed Version:
#    - Proper constructor: __init__
#    - Correct indentation and logic flow
#    - Fixed variable names and syntax