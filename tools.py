from crewai.tools import tool
from db import add_log, get_logs

@tool("Log Habit Tool")
def log_habit_tool(habit_name: str, status: str) -> str:
    """Logs a habit's status for today. status must be 'done' or 'missed'."""
    add_log(habit_name, status)
    return f"Logged: {habit_name} - {status}"

@tool("Analyze Habit Tool")
def analyze_habit_tool(habit_name: str) -> str:
    """Calculates total logs, completion percentage, and current streak for a habit."""
    logs = get_logs(habit_name)
    if not logs:
        return f"No data found for {habit_name}"

    total = len(logs)
    done = sum(1 for _, status, _ in logs if status == "done")
    completion_pct = round((done / total) * 100, 1)

    streak = 0
    for _, status, _ in reversed(logs):
        if status == "done":
            streak += 1
        else:
            break

    return (f"Habit: {habit_name} | Total logs: {total} | "
            f"Completed: {done} | Completion%: {completion_pct} | Current streak: {streak} days")