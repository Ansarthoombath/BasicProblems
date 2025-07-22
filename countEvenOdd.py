arr = [1, 2, 3, 4, 5]
even = sum(1 for i in arr if i % 2 == 0)
odd = sum(1 for i in arr if i % 2 != 0)
print("Even:", even, "Odd:", odd)  # Output: Even: 2 Odd: 3