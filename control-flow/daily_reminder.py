#!/bin/bash
# Get user input
task = input("Enter your most important task for today: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound (yes or no): ").lower()

# Reminder message
reminder = f"Don't forget to {task} today."

# Modify reminder based on priority (Match Case)
match priority:
    case "high":
        reminder = f"**Important!** {reminder}"
    case "medium":
        reminder = f"{reminder} (Consider completing it if you have time)"
    case _:  # Default case for unexpected priority levels
        reminder = f"Reminder: {task}"

# Add urgency if time-bound
if time_bound == "yes":
    reminder += "  This requires immediate attention today!"

# Print the reminder
print(reminder)
