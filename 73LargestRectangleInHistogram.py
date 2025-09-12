def largestRectangleArea(heights):
    stack = []          # stack to store indices of increasing bars
    max_area = 0
    # Add a sentinel 0 at the end to flush out remaining bars
    for i, h in enumerate(heights + [0]):
        # While current height < height of last bar in stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]               # height of rectangle
            # width = full width if stack empty, else distance to previous smaller bar
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)   # push current index
    return max_area

# Example
print(largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
