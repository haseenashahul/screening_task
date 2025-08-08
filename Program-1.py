class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == '+':
            return self.a + self.b
        elif self.operation == '-':
            return self.a - self.b
        elif self.operation == '*':
            return self.a * self.b
        elif self.operation == '/':
            if self.b == 0:
                return "Cannot divide by zero"
            return self.a / self.b
        else:
            return "Invalid operation type"



a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

calc = Calculator(a, b, op)
print("Result:", calc.calculate())
