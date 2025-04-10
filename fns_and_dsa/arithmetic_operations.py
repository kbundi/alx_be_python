def perform_operation(num1, num2, operation):
    operations =  {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
     }

    for x,y in operations.items():
        if operation == x:
            return num1,y,num2
    print(f"invalid operation '{operation}'. Supported operations are:{', '.join(operations)}")

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a/b

