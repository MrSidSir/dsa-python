# 15. Next Greater Element
# Topic: Stack
# Real-World Use: Weather prediction, processing sensor data, stock analysis.

def next_greater(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result

print(next_greater([4, 5, 2, 25]))
# ✅ Output: [5, 25, 25, -1]



# ✅ Step-by-Step Workflow
# Given: arr = [4, 5, 2, 25]

# We traverse from right to left to find the nearest greater element on the right side.

# i	arr[i]	Stack Before	Action (Pop?)	Stack After	result[i]
# 3	25	[]	No	[25]	-1
# 2	2	[25]	No	[25, 2]	25
# 1	5	[25, 2] → [25]	Yes (2 < 5)	[25, 5]	25
# 0	4	[25, 5]	No	[25, 5, 4]	5

# ✅ Final Output: [5, 25, 25, -1]

# ✅ Real-World Applications
# 1. 🌦️ Weather Forecasting (Sensor Data)
# Say you have temperature readings for 7 days.

# You want to know when will it be hotter next?

# This algorithm finds the next hotter day efficiently.

# 2. 📉 Stock Market
# Used to find the next higher stock price in historical data.

# Helps in making buy/sell decisions.

# 3. 📡 Sensor Monitoring (IoT)
# In manufacturing or automation, sensors report values.

# You can detect next higher pressure, temperature, or signal using this logic.

# ✅ Summary
# Algorithm Type: Monotonic Stack (Decreasing)

# Time Complexity: O(n)

# Use Cases: Weather, Stocks, Sensor Alerts

# Key Insight: Works right-to-left, keeps possible greater elements on the stack.