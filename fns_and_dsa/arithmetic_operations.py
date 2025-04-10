def perform_operation(num1,num2,operation):
    operators =  {
        'add': addition,
        'subtract': subtraction,
        'multiply': multiplication,
        'divide': division
     }

    if operation not in operators:
        raise ValueError("please enter correct operator, ie add, subtract,divide")
    return operators[operation](num1,num2)

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

