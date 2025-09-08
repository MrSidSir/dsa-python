# 1. Find maximum of two numbers
a = 10
b = 20
print("Max is", a if a > b else b)

# 2. Check if number is prime
num = 29
if num > 1:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
else:
    print(num, "is not prime")

# 3. Fibonacci sequence up to n terms
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
print()  # New line after fibonacci sequence

# 4. Factorial (iterative)
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial is", fact)

# 5. Factorial (recursive)
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("Factorial (recursive):", factorial_recursive(5))

# 6. Reverse a string
s = "hello"
print("Reversed string:", s[::-1])

# 7. Check palindrome
s = "madam"
print("Palindrome" if s == s[::-1] else "Not palindrome")

# 8. Largest element in array
arr = [10, 25, 43, 5]
print("Largest:", max(arr))

# 9. Second largest
arr = [10, 25, 43, 5]
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second largest:", second)

# 10. Bubble sort
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)

#output:-Max is 20
# 29 is prime
# 0 1 1 2 3 5 8 13 21 34
# Factorial is 120
# Factorial (recursive): 120
# Reversed string: olleh
# Palindrome
# Largest: 43
# Second largest: 25
# Sorted array: [11, 12, 22, 25, 34, 64, 90]