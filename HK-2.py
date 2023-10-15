def can_stack_cubes(test_cases):
    results = []
    for cubes in test_cases:
        n, blocks = cubes[0], cubes[1]

        left = 0
        right = n - 1
        prev = float('inf')

        while left <= right:
            if blocks[left] >= blocks[right] and blocks[left] <= prev:
                prev = blocks[left]
                left += 1
            elif blocks[right] >= blocks[left] and blocks[right] <= prev:
                prev = blocks[right]
                right -= 1
            else:
                results.append("No")
                break
        else:
            results.append("Yes")

    return results

if __name__ == '__main__':
    t = int(input().strip())
    test_cases = []
    
    for _ in range(t):
        n = int(input().strip())
        blocks = list(map(int, input().split()))
        test_cases.append((n, blocks))
    
    results = can_stack_cubes(test_cases)
    for result in results:
        print(result)
---_-----------------------------------------------------
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

if len(sys.argv) != 4:
    print("Usage: calculator.py <operation> <operand1> <operand2>")
    sys.exit(1)

operation = sys.argv[1]
operand1 = float(sys.argv[2])
operand2 = float(sys.argv[3])

if operation == 'add':
    result = add(operand1, operand2)
elif operation == 'subtract':
    result = subtract(operand1, operand2)
elif operation == 'multiply':
    result = multiply(operand1, operand2)
elif operation == 'divide':
    result = divide(operand1, operand2)
else:
    print("Invalid operation. Available operations: add, subtract, multiply, divide")
    sys.exit(1)

print(f"Result: {result}")
