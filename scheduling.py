from datetime import datetime, timedelta

# Define a simple task structure
class Task:
    def __init__(self, name, hours_required, due_date):
        self.name = name
        self.hours_required = hours_required
        self.due_date = due_date

def schedule_tasks(tasks, hours_per_week, start_day = datetime.now().date()):
    tasks.sort(key=lambda x: x.due_date)
    start_day = datetime.now().date()
    day_of_week = start_day.weekday()
    schedule = {}
    for task in tasks:
        hours_allocated = 0
        while hours_allocated < task.hours_required:
            # Check if the task's due date is before the current scheduling day
            if task.due_date.date() < start_day:
                print(f"Error: Cannot schedule '{task.name}' by its due date ({task.due_date.date()}).")
                return {}
            if start_day not in schedule:
                schedule[start_day] = []
            available_hours_today = hours_per_week[day_of_week] - sum(t.hours_required for t in schedule[start_day])
            if available_hours_today > 0:
                alloc_hours = min(task.hours_required - hours_allocated, available_hours_today)
                schedule[start_day].append(Task(task.name, alloc_hours, task.due_date))
                hours_allocated += alloc_hours
            start_day += timedelta(days=1)
            day_of_week = (day_of_week + 1) % 7
    return schedule

def print_schedule(scheduled_tasks):
    for day, tasks in scheduled_tasks.items():
        print(f"Day {day}:")
        for task in tasks:
            print(f"  - {task.name}: {task.hours_required} hour(s)")

# Example tasks and hours per week
tasks = [
    Task("Task 1", 2, datetime.strptime("2024-04-05", "%Y-%m-%d")),
    Task("Task 2", 5, datetime.strptime("2024-04-01", "%Y-%m-%d")),
    Task("Task 3", 4, datetime.strptime("2024-04-03", "%Y-%m-%d")),
    Task("Task 4", 3, datetime.strptime("2024-04-02", "%Y-%m-%d")),
]
hours_per_week = [4, 4, 4, 4, 4, 0, 0]  # Monday to Sunday

# Schedule tasks and print the schedule
scheduled_tasks = schedule_tasks(tasks, hours_per_week)
print_schedule(scheduled_tasks)
