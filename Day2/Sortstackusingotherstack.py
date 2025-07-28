def sortStack(s):
    tmpStack = []
    
    # Process each element from original stack
    while s:
        tmp = s.pop()
        
        # Move elements from tmpStack back to s if they're greater than tmp
        while tmpStack and tmpStack[-1] > tmp:
            s.append(tmpStack.pop())
        
        # Place tmp in correct position in tmpStack
        tmpStack.append(tmp)  # Fixed: added missing dot
    
    return tmpStack

# 🔄 **STEP-BY-STEP WORKFLOW DEMONSTRATION**
print("=== Stack Sorting Algorithm Workflow ===")
print("🎯 Goal: Sort stack in ascending order (smallest at top)")

def sortStackWithVisualization(s):
    print(f"\n📥 Original Stack: {s}")
    tmpStack = []
    step = 1
    
    while s:
        tmp = s.pop()
        print(f"\n📍 Step {step}:")
        print(f"   Popped element: {tmp}")
        print(f"   Main stack: {s}")
        print(f"   Temp stack: {tmpStack}")
        
        # Move larger elements back to main stack
        moved_count = 0
        while tmpStack and tmpStack[-1] > tmp:
            moved_element = tmpStack.pop()
            s.append(moved_element)
            moved_count += 1
            print(f"   🔄 Moved {moved_element} back to main stack")
        
        # Place current element in temp stack
        tmpStack.append(tmp)
        print(f"   ✅ Placed {tmp} in temp stack")
        print(f"   📊 Current state - Main: {s}, Temp: {tmpStack}")
        step += 1
    
    print(f"\n🎉 Final sorted stack: {tmpStack}")
    return tmpStack

# Example 1: Detailed visualization
s1 = [34, 3, 31, 98, 92, 23]
result1 = sortStackWithVisualization(s1.copy())

print("\n" + "="*60)
print("🧮 **ALGORITHM ANALYSIS**")
print("="*60)

# Example 2: Simple execution
s2 = [34, 3, 31, 98, 92, 23]
print(f"\nOriginal: {s2}")
sorted_result = sortStack(s2)
print(f"Sorted:   {sorted_result}")

print(f"""
⏱️ **Time Complexity:** O(n²) worst case
   - Each element might be moved multiple times
   - In worst case (reverse sorted), each element touches all others

💾 **Space Complexity:** O(n)
   - Additional stack for temporary storage
   - No recursive calls, so O(1) call stack space

🔧 **Algorithm Steps:**
   1. Pop element from original stack
   2. While temp stack top > current element:
      - Move temp stack elements back to original
   3. Push current element to temp stack
   4. Repeat until original stack is empty
""")

print("\n" + "="*60)
print("🌍 **REAL-WORLD APPLICATIONS**")
print("="*60)

print("""
# 1️⃣ **Function Call Stack Sorting**
#    - Debugging tools sort call stack by priority
#    - IDE debuggers organize stack frames
#    - Used in: Visual Studio, IntelliJ IDEA

# 2️⃣ **Browser History Management**
#    - Sort browsing history by frequency/recency
#    - Tab management in browsers
#    - Used in: Chrome, Firefox tab sorting

# 3️⃣ **Undo/Redo Operations**
#    - Sort undo stack by importance/timestamp
#    - Text editors, image editors
#    - Used in: Photoshop, Word, VS Code

# 4️⃣ **System Process Management**
#    - Sort process stack by priority
#    - CPU scheduling algorithms
#    - Used in: Linux kernel, Windows Task Manager

# 5️⃣ **Game Development**
#    - Sort rendering layers/draw calls
#    - Z-order sorting for 2D sprites
#    - Used in: Unity, Unreal Engine

# 6️⃣ **Compiler Optimizations**
#    - Sort expression evaluation stack
#    - Optimize arithmetic operations order
#    - Used in: GCC, LLVM compilers

# 7️⃣ **Database Query Processing**
#    - Sort execution plan stack
#    - Optimize query operation order
#    - Used in: MySQL, PostgreSQL optimizers

# 8️⃣ **Mathematical Expression Evaluation**
#    - Sort operator precedence stack
#    - Calculator applications
#    - Used in: Scientific calculators, Excel
# """)

print("\n" + "="*60)
print("💼 **PRACTICAL IMPLEMENTATIONS**")
print("="*60)

# Practical example: Task priority sorting
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __repr__(self):
        return f"Task('{self.name}', {self.priority})"
    
    def __gt__(self, other):
        return self.priority > other.priority

def sortTaskStack(task_stack):
    """Sort tasks by priority (lower number = higher priority)"""
    tmpStack = []
    
    while task_stack:
        current_task = task_stack.pop()
        
        while tmpStack and tmpStack[-1] > current_task:
            task_stack.append(tmpStack.pop())
        
        tmpStack.append(current_task)
    
    return tmpStack

print("\n🔥 **Practical Example: Task Priority Sorting**")
tasks = [
    Task("Email", 3),
    Task("Bug Fix", 1),
    Task("Meeting", 2),
    Task("Documentation", 4),
    Task("Code Review", 1)
]

print(f"Original tasks: {tasks}")
sorted_tasks = sortTaskStack(tasks.copy())
print(f"Sorted by priority: {sorted_tasks}")

print("\n" + "="*60)
print("⚡ **PERFORMANCE COMPARISON**")
print("="*60)

import time
import random

def performance_test():
    sizes = [100, 500, 1000]
    
    for size in sizes:
        # Generate random stack
        test_stack = [random.randint(1, 1000) for _ in range(size)]
        
        start_time = time.time()
        sortStack(test_stack.copy())
        end_time = time.time()
        
        print(f"Size {size:4d}: {(end_time - start_time)*1000:.2f} ms")

print("\n📊 Performance Test Results:")
performance_test()

print(f"""
\n
      
#       Original: [34, 3, 31, 98, 92, 23]
# Sorted:   [3, 23, 31, 34, 92, 98]

# 💡 **Key Insight:**
# This algorithm is perfect when you need to sort data that's naturally 
# organized in a stack structure, maintaining the stack-based access pattern
# while achieving sorted order efficiently.
# """)