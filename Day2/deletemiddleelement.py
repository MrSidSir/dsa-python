# 13. Delete middle element of stack
# ✔ Workflow: Recursive deletion reaching middle index.

def deleteMid(stack, k):
    # Base case: reached middle element
    if k == 1:
        stack.pop()  # Delete the middle element
        return
    
    # Store top element temporarily
    temp = stack.pop()
    
    # Recursive call to reach middle
    deleteMid(stack, k-1)
    
    # Push back the stored element
    stack.append(temp)  # Fixed: missing append

# 🔄 **STEP-BY-STEP WORKFLOW DEMONSTRATION**
print("=== Delete Middle Element Algorithm Workflow ===")
print("🎯 Goal: Remove middle element from stack using recursion")

def deleteMidWithVisualization(stack, k, original_k=None, depth=0):
    if original_k is None:
        original_k = k
    
    indent = "  " * depth
    print(f"{indent}📍 Call {depth + 1}: k={k}, Stack: {stack}")
    
    # Base case: reached middle element
    if k == 1:
        middle_element = stack.pop()
        print(f"{indent}🎯 BASE CASE: Deleting middle element '{middle_element}'")
        print(f"{indent}📚 Stack after deletion: {stack}")
        return
    
    # Store top element temporarily
    temp = stack.pop()
    print(f"{indent}📤 Popped and stored: {temp}")
    print(f"{indent}📚 Stack after pop: {stack}")
    
    # Recursive call to reach middle
    print(f"{indent}🔄 Recursive call with k={k-1}")
    deleteMidWithVisualization(stack, k-1, original_k, depth + 1)
    
    # Push back the stored element
    stack.append(temp)
    print(f"{indent}📥 Pushed back: {temp}")
    print(f"{indent}📚 Stack after push: {stack}")

# Example 1: Odd length stack
print("\n" + "="*60)
print("📝 Example 1: Odd Length Stack [1,2,3,4,5]")
print("Middle position: 3 (1-indexed)")

stack1 = [1, 2, 3, 4, 5]
original_stack1 = stack1.copy()
middle_pos1 = len(stack1) // 2 + 1

print(f"Original stack: {original_stack1}")
print(f"Stack length: {len(stack1)}, Middle position: {middle_pos1}")
print("\n🔄 Recursive Execution:")

deleteMidWithVisualization(stack1, middle_pos1)
print(f"\n✅ Final Result: {stack1}")

# Example 2: Even length stack
print("\n" + "="*60)
print("📝 Example 2: Even Length Stack [1,2,3,4]")

stack2 = [1, 2, 3, 4]
original_stack2 = stack2.copy()
middle_pos2 = len(stack2) // 2 + 1

print(f"Original stack: {original_stack2}")
print(f"Stack length: {len(stack2)}, Middle position: {middle_pos2}")
print("\n🔄 Recursive Execution:")

deleteMidWithVisualization(stack2, middle_pos2)
print(f"\n✅ Final Result: {stack2}")

print("\n" + "="*60)
print("🧮 **ALGORITHM ANALYSIS**")
print("="*60)

# print(f"""
# 🔧 **Algorithm Logic:**
#    1. Use recursion to reach middle element
#    2. Pop elements and store them in recursive call stack
#    3. When k=1, delete the middle element (base case)
#    4. Return and push back all stored elements

# 📐 **Middle Position Calculation:**
#    - For odd length n: middle = n//2 + 1
#    - For even length n: middle = n//2 + 1 (upper middle)
#    - Examples: [1,2,3] → middle=2, [1,2,3,4] → middle=3

# ⏱️ **Time Complexity:** O(n)
#    - Visit each element above middle once
#    - Each recursive call does O(1) work

# 💾 **Space Complexity:** O(n)
#    - Recursive call stack depth = n/2
#    - Each call stores one element

# 🎯 **Key Properties:**
#    ✅ Maintains stack order (LIFO)
#    ✅ Uses only stack operations (push/pop)
#    ✅ Elegant recursive solution
#    ✅ No additional data structures needed
# """)

print("\n" + "="*60)
print("🌍 **REAL-WORLD APPLICATIONS**")
print("="*60)

# print("""
# 1️⃣ **Undo/Redo Systems**
#    - Remove middle operation from undo stack
#    - Text editors when user wants to skip certain actions
#    - Used in: Adobe Photoshop, Microsoft Word

# 2️⃣ **Browser History Management**
#    - Delete specific page from middle of history
#    - Clean up browsing sessions
#    - Used in: Chrome, Firefox, Safari

# 3️⃣ **Game Development**
#    - Remove middle save state from save stack
#    - Clean up game state histories
#    - Used in: RPG games, strategy games

# 4️⃣ **Call Stack Debugging**
#    - Remove specific function call from debug stack
#    - Skip certain stack frames during debugging
#    - Used in: IDE debuggers, profiling tools

# 5️⃣ **Memory Management**
#    - Clean up middle entries in allocation stack
#    - Garbage collection optimizations
#    - Used in: JVM, .NET CLR, Python interpreter

# 6️⃣ **Expression Evaluation**
#    - Remove redundant operations from evaluation stack
#    - Compiler optimizations
#    - Used in: GCC, LLVM optimizers

# 7️⃣ **Network Stack Processing**
#    - Remove middle layers from protocol stack
#    - Network packet processing
#    - Used in: TCP/IP implementations, routers

# 8️⃣ **Database Transaction Logs**
#    - Remove middle transaction from log stack
#    - Database recovery operations
#    - Used in: MySQL, PostgreSQL, Oracle
# """)

print("\n" + "="*60)
print("💼 **PRACTICAL IMPLEMENTATION SCENARIOS**")
print("="*60)

# Practical example: Task management system
class TaskManager:
    def __init__(self):
        self.task_stack = []
    
    def add_task(self, task):
        self.task_stack.append(task)
        print(f"Added task: {task}")
    
    def remove_middle_task(self):
        if not self.task_stack:
            print("No tasks to remove")
            return
        
        print(f"Tasks before removal: {self.task_stack}")
        middle_pos = len(self.task_stack) // 2 + 1
        deleteMid(self.task_stack, middle_pos)
        print(f"Tasks after removing middle: {self.task_stack}")
    
    def show_tasks(self):
        print(f"Current tasks: {self.task_stack}")

print("\n🔥 **Practical Example: Task Management System**")
task_manager = TaskManager()

# Add some tasks
tasks = ["Email", "Meeting", "Code Review", "Documentation", "Testing"]
for task in tasks:
    task_manager.add_task(task)

print(f"\nAll tasks added: {task_manager.task_stack}")
task_manager.remove_middle_task()

# Memory usage demonstration
print("\n" + "="*60)
print("📊 **MEMORY USAGE ANALYSIS**")
print("="*60)

def analyze_recursion_depth(n):
    """Analyze recursion depth for different stack sizes"""
    depths = []
    for size in range(1, n+1):
        middle_pos = size // 2 + 1
        recursion_depth = middle_pos - 1
        depths.append((size, middle_pos, recursion_depth))
    return depths

print("\n📈 Recursion Depth Analysis:")
print("Stack Size | Middle Pos | Recursion Depth")
print("-" * 40)

analysis = analyze_recursion_depth(10)
for size, mid_pos, depth in analysis:
    print(f"{size:^10} | {mid_pos:^10} | {depth:^15}")

print("\n" + "="*60)
print("⚖️ **ALGORITHM COMPARISON**")
print("="*60)

# Alternative iterative approach for comparison
def deleteMidIterative(stack, k):
    """Alternative iterative approach using auxiliary stack"""
    temp_stack = []
    
    # Pop k-1 elements to temporary stack
    for _ in range(k-1):
        if stack:
            temp_stack.append(stack.pop())
    
    # Remove the middle element
    if stack:
        stack.pop()
    
    # Push back elements from temporary stack
    while temp_stack:
        stack.append(temp_stack.pop())

print("\n🔄 **Comparison: Recursive vs Iterative**")

# Test both approaches
test_stack_rec = [1, 2, 3, 4, 5]
test_stack_iter = [1, 2, 3, 4, 5]
middle = len(test_stack_rec) // 2 + 1

print(f"Original stack: {test_stack_rec}")

# Recursive approach
deleteMid(test_stack_rec, middle)
print(f"Recursive result: {test_stack_rec}")

# Iterative approach
deleteMidIterative(test_stack_iter, middle)
print(f"Iterative result: {test_stack_iter}")

# print(f"""
# 📊 **Approach Comparison:**
#                  | Recursive | Iterative
# -----------------|-----------|-----------
# Time Complexity  | O(n)      | O(n)
# Space Complexity | O(n)      | O(n)
# Code Simplicity  | High      | Medium
# Stack Usage      | Call Stack| Auxiliary Stack
# Readability      | High      | Medium

# 💡 **When to Use:**
# - Recursive: When code simplicity is priority
# - Iterative: When call stack depth is a concern
# """)

print("\n" + "="*60)
print("🔧 **CODE FIXES APPLIED**")
print("="*60)



# Final demonstration with original example
print("\n" + "="*60)
print("🎯 **FINAL DEMONSTRATION - Original Example**")
print("="*60)

stack = [1, 2, 3, 4, 5]
print(f"Original stack: {stack}")
deleteMid(stack, len(stack)//2 + 1)
print(f"After deleting middle: {stack}")

# 🎯 **FINAL DEMONSTRATION - Original Example**        
# ============================================================
# Original stack: [1, 2, 3, 4, 5]
# After deleting middle: [1, 2, 4, 5]

