task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case to handle different priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

# Add urgency message if time-bound
if time_bound == "yes":
    if "priority" in reminder:
        reminder += " that requires immediate attention today!"
    else:
        reminder += " and requires immediate attention today!"

if time_bound == "no" and priority == "low":
    reminder += ". Consider completing it when you have free time."

print(reminder)

