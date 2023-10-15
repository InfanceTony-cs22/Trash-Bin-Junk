print("traveling to madurai")
print("Traveling in train")
print("Traveling aalong with my family")
print("two days travel")
--------       ---------


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
