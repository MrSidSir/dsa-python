# 1. Sum of all elements
arr = [1,2,3,4,5]
print("Sum:", sum(arr))

# 2. Average of elements
print("Average:", sum(arr)/len(arr))

# 3. Frequency of elements
freq = {}
for i in arr:
    freq[i] = freq.get(i,0)+1
print("Frequency:", freq)

# 4. Check anagram
s1 = "listen"
s2 = "silent"
print("Anagram" if sorted(s1)==sorted(s2) else "Not anagram")

# 5. Count vowels
s = "hello world"
vowels = 'aeiou'
count = sum(1 for c in s if c in vowels)
print("Vowel count:", count)

# 6. Simple class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name, "Age:", self.age)

s1 = Student("John", 22)
s1.display()

# 7. Armstrong number
num = 153
n = len(str(num))
sum1 = sum(int(d)**n for d in str(num))
print("Armstrong" if num==sum1 else "Not Armstrong")

# 8. GCD of two numbers
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
print("GCD:", gcd(48,18))

# 9. LCM of two numbers
def lcm(a,b):
    return abs(a*b)//gcd(a,b)
print("LCM:", lcm(4,6))

# 10. Selection sort
arr = [64,25,12,22,11]
n = len(arr)
for i in range(n):
    min_idx = i
    for j in range(i+1,n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Sorted array:", arr)
#   output:-Sum: 15
# Average: 3.0
# Frequency: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
# Anagram
# Vowel count: 3
# Name: John Age: 22
# Armstrong
# GCD: 6
# LCM: 12
# Sorted array: [11, 12, 22, 25, 64]