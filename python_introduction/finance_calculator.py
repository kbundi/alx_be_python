#!/bin/bash
# User Input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings (Assuming 5% annual interest rate)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display Results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings with 5% interest: ${projected_savings:.2f}")

