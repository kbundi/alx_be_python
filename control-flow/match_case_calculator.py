#!/bin/bash
 num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Choose the operation (+, -, *, /): ")

  match operator:
    case "+":
      result = num1 + num2
    case "-":
      result = num1 - num2
    case "*":
      result = num1 * num2
    case "/":
      if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return
      else:
        result = num1 / num2
    case _:
      print("Invalid operator. Please choose from +, -, *, /")