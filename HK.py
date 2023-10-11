from itertools import product

# Read input values
k, m = map(int, input().split())

# Create a list of lists to store the elements from the input
lists = []
for _ in range(k):
    elements = list(map(int, input().split()))[1:]
    lists.append(elements)

# Initialize the maximum result to be the smallest possible integer
max_result = float('-inf')

# Iterate through all possible combinations of elements
for combination in product(*lists):
    result = sum(x ** 2 for x in combination) % m
    max_result = max(max_result, result)

# Print the maximum result
print(max_result)
