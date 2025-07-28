def evalPrefix(exp):
    stack = []
    # Scan from right to left (reverse the expression)
    for token in exp[::-1]:  # Fixed: 'inn' to 'in', proper slicing
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            # Handle positive and negative numbers
            stack.append(int(token))
        else:
            # Pop two operands and apply operator
            a = stack.pop()  # First operand
            b = stack.pop()  # Second operand
            
            # Perform operation based on operator
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b  # Integer division
            elif token == '^' or token == '**':
                result = a ** b
            else:
                raise ValueError(f"Unknown operator: {token}")
            
            stack.append(result)
    
    return stack[0]  # Final result

# 🔄 **STEP-BY-STEP WORKFLOW DEMONSTRATION**
print("=== Prefix Expression Evaluation Workflow ===")
print("🎯 Goal: Evaluate prefix notation expressions (operator comes first)")

def evalPrefixWithVisualization(exp):
    print(f"\n📥 Prefix Expression: {' '.join(exp)}")
    print(f"📊 Scanning Direction: Right to Left ←")
    
    stack = []
    step = 1
    
    # Reverse the expression for right-to-left scanning
    reversed_exp = exp[::-1]
    print(f"🔄 Reversed for scanning: {' '.join(reversed_exp)}")
    
    for i, token in enumerate(reversed_exp):
        print(f"\n📍 Step {step} - Processing: '{token}'")
        print(f"   Position: {len(exp) - 1 - i} (from right)")
        
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
            print(f"   ✅ Operand found: {token}")
            print(f"   📚 Stack after push: {stack}")
        else:
            print(f"   🔧 Operator found: {token}")
            a = stack.pop()
            b = stack.pop()
            print(f"   📤 Popped operands: {a}, {b}")
            
            if token == '+':
                result = a + b
                operation = f"{a} + {b}"
            elif token == '-':
                result = a - b
                operation = f"{a} - {b}"
            elif token == '*':
                result = a * b
                operation = f"{a} * {b}"
            elif token == '/':
                result = a // b
                operation = f"{a} // {b}"
            elif token == '^' or token == '**':
                result = a ** b
                operation = f"{a} ** {b}"
            
            print(f"   🧮 Calculation: {operation} = {result}")
            stack.append(result)
            print(f"   📚 Stack after operation: {stack}")
        
        step += 1
    
    final_result = stack[0]
    print(f"\n🎉 Final Result: {final_result}")
    return final_result

# Example 1: Detailed visualization
exp1 = ['-', '*', '5', '4', '3']  # Represents: - (* 5 4) 3 = (5*4) - 3 = 20 - 3 = 17
print("="*70)
print("📝 Example 1: ['-', '*', '5', '4', '3']")
print("Mathematical meaning: - (* 5 4) 3 = (5×4) - 3 = 20 - 3 = 17")
result1 = evalPrefixWithVisualization(exp1)

# Example 2: More complex expression
print("\n" + "="*70)
print("📝 Example 2: ['+', '-', '10', '5', '*', '2', '3']")
print("Mathematical meaning: + (- 10 5) (* 2 3) = (10-5) + (2×3) = 5 + 6 = 11")
exp2 = ['+', '-', '10', '5', '*', '2', '3']
result2 = evalPrefixWithVisualization(exp2)

print("\n" + "="*70)
print("🧮 **ALGORITHM ANALYSIS**")
print("="*70)

# print(f"""
# 📋 **Prefix Notation (Polish Notation):**
#    - Operator comes BEFORE operands
#    - Example: + 3 4 means 3 + 4
#    - Invented by Jan Łukasiewicz in 1924

# 🔄 **Algorithm Steps:**
#    1. Scan expression from RIGHT to LEFT
#    2. If operand → push to stack
#    3. If operator → pop 2 operands, compute, push result
#    4. Final stack top is the answer

# ⏱️ **Time Complexity:** O(n)
#    - Single pass through expression
#    - Each element processed exactly once

# 💾 **Space Complexity:** O(n)
#    - Stack space for operands
#    - Worst case: all operands before operators

# 🎯 **Key Advantages:**
#    ✅ No parentheses needed
#    ✅ No operator precedence issues
#    ✅ Easy to evaluate programmatically
#    ✅ Efficient for compilers
# """)

print("\n" + "="*70)
print("🌍 **REAL-WORLD APPLICATIONS**")
print("="*70)

# print("""
# 1️⃣ **Compiler Design**
#    - Internal representation of expressions
#    - Code generation for stack machines
#    - Used in: GCC, LLVM, Java bytecode

# 2️⃣ **Calculator Applications**
#    - Scientific calculators internal processing
#    - Expression parsers
#    - Used in: HP calculators, Mathematica

# 3️⃣ **Database Query Engines**
#    - SQL expression evaluation
#    - Query optimization trees
#    - Used in: PostgreSQL, MySQL, Oracle

# 4️⃣ **Spreadsheet Software**
#    - Formula evaluation engines
#    - Cell dependency resolution
#    - Used in: Excel, Google Sheets, LibreOffice

# 5️⃣ **Programming Language Interpreters**
#    - LISP language evaluation
#    - Functional programming languages
#    - Used in: Scheme, Clojure, Emacs Lisp

# 6️⃣ **Mathematical Software**
#    - Computer algebra systems
#    - Symbolic computation
#    - Used in: Maple, Mathematica, SageMath

# 7️⃣ **Game Engines**
#    - AI decision trees
#    - Scripting language evaluation
#    - Used in: Unity, Unreal Engine

# 8️⃣ **Hardware Design**
#    - Circuit logic evaluation
#    - FPGA programming
#    - Used in: VHDL, Verilog compilers
# """)

print("\n" + "="*70)
print("💼 **PRACTICAL IMPLEMENTATIONS**")
print("="*70)

# Enhanced version with error handling
def evalPrefixAdvanced(exp):
    """Advanced prefix evaluator with error handling and float support"""
    if not exp:
        raise ValueError("Empty expression")
    
    stack = []
    
    try:
        for token in exp[::-1]:
            if token.replace('.', '').replace('-', '').isdigit():
                # Handle integers and floats
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError(f"Insufficient operands for operator '{token}'")
                
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                
                operations = {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y if y != 0 else float('inf'),
                    '^': lambda x, y: x ** y,
                    '**': lambda x, y: x ** y,
                    '%': lambda x, y: x % y if y != 0 else 0
                }
                
                if token not in operations:
                    raise ValueError(f"Unknown operator: '{token}'")
                
                result = operations[token](a, b)
                stack.append(result)
        
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
        
        return stack[0]
    
    except IndexError:
        raise ValueError("Invalid expression: insufficient operands")

# Test cases
print("\n🧪 **Advanced Test Cases:**")
test_cases = [
    (['+', '3', '4'], "Simple addition: + 3 4"),
    (['-', '*', '5', '4', '3'], "Complex: - (* 5 4) 3"),
    (['+', '-', '10', '5', '*', '2', '3'], "Multi-op: + (- 10 5) (* 2 3)"),
    (['^', '2', '3'], "Exponentiation: ^ 2 3"),
    (['/', '+', '15', '5', '4'], "Division: / (+ 15 5) 4"),
]

for exp, description in test_cases:
    try:
        result = evalPrefixAdvanced(exp)
        print(f"✅ {description}")
        print(f"   Expression: {' '.join(exp)} = {result}")
    except Exception as e:
        print(f"❌ Error in {description}: {e}")

print("\n" + "="*70)
print("🔧 **COMPARISON WITH OTHER NOTATIONS**")
print("="*70)

# Comparison table
expressions = [
    ("Infix", "3 + 4 * 5", "Human-readable, needs precedence rules"),
    ("Prefix", "+ 3 * 4 5", "No precedence needed, operator first"),
    ("Postfix", "3 4 5 * +", "No precedence needed, operator last"),
]

print("\n📊 Same mathematical expression in different notations:")
print("Result: 3 + (4 × 5) = 3 + 20 = 23\n")

for notation, expr, note in expressions:
    print(f"{notation:8s}: {expr:12s} - {note}")

# Conversion example
def infixToPrefix(infix):
    """Simple infix to prefix converter for demonstration"""
    # This is a simplified version for basic expressions
    # Real implementation would need proper parsing
    conversions = {
        "3 + 4": ["+ 3 4"],
        "3 + 4 * 5": ["+ 3 * 4 5"],
        "(3 + 4) * 5": ["* + 3 4 5"],
        "10 - 5 + 2": ["+ - 10 5 2"]
    }
    return conversions.get(infix, ["Conversion not implemented"])

print(f"\n🔄 **Quick Conversion Examples:**")
infix_examples = ["3 + 4", "3 + 4 * 5", "(3 + 4) * 5"]
for infix in infix_examples:
    prefix = infixToPrefix(infix)[0]
    print(f"Infix:  {infix:12s} → Prefix: {prefix}")

print(f"""
# \n🔧 **CODE FIXES APPLIED:**
# ❌ Original Issues:
#    - 'inn' → 'in' (syntax error in for loop)
#    - Missing proper indentation
#    - Used eval() (security risk)
#    - No error handling for invalid expressions

# ✅ Fixed Version:
#    - Correct loop syntax with proper slicing
#    - Safe operator evaluation without eval()
#    - Comprehensive error handling
#    - Support for multiple operators and edge cases
#    - Detailed visualization and step-by-step tracking

# 💡 **Key Insights:**
#    - Prefix notation eliminates need for parentheses
#    - Right-to-left scanning is crucial for correct evaluation
#    - Stack-based evaluation is efficient and straightforward
#    - Widely used in compiler design and mathematical software
# """)

# Final demonstration
print("\n" + "="*70)
print("🎯 **FINAL DEMONSTRATION**")
print("="*70)

original_exp = ['-', '*', '5', '4', '3']
result = evalPrefix(original_exp)
print(f"Original Expression: {' '.join(original_exp)}")
print(f"Mathematical Form: - (* 5 4) 3 = (5×4) - 3 = 20 - 3")
print(f"Final Result: {result}")

# 🎯 **FINAL DEMONSTRATION**
# ======================================================================
# Original Expression: - * 5 4 3
# Mathematical Form: - (* 5 4) 3 = (5×4) - 3 = 20 - 3  
# Final Result: 17
