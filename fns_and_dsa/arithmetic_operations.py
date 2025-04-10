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


if operation == 'add':
    return num1+num2

elif operation == 'subtract':
    return num1-num2

elif operation == 'multiply':
    return num1*num2

elif operation == 'divide':
    if num2 == '0':
        return "Error Divieion by Zero"
    else: return num1/num2

