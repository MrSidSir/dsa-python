# 14. Stock span problem
# ✔ Workflow: Stack to track indices with lesser price.

def stockSpan(prices):
    stack, res = [], [0] * len(prices)
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        res[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    
    return res

print("stock span:", stockSpan([100, 80, 60, 70, 60, 75, 85]))
# ✅ Output: [1, 1, 1, 2, 1, 4, 6]
