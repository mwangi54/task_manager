from datetime import datetime

def validate_task_title(title):
    """Validate that the task title is not empty and is a string."""
    if not title or not isinstance(title, str):
        raise ValueError("Task title cannot be empty and must be a string.")
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty or just whitespace.")
    if len(title) > 100:
        raise ValueError("Task title must be 100 characters or less.")
    return title.strip()

def validate_task_description(description):
    """Validate that the task description is a string (can be empty)."""
    if not isinstance(description, str):
        raise ValueError("Task description must be a string.")
    if len(description) > 500:
        raise ValueError("Task description must be 500 characters or less.")
    return description.strip()

def validate_due_date(due_date):
    """Validate that the due date is in YYYY-MM-DD format and is not in the past."""
    try:
        # Try to parse the date
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
        
        # Check if the date is in the past
        if parsed_date.date() < datetime.now().date():
            raise ValueError("Due date cannot be in the past.")
        
        return parsed_date.strftime("%Y-%m-%d")
    except ValueError as e:
        if "unconverted data remains" in str(e) or "does not match format" in str(e):
            raise ValueError("Due date must be in YYYY-MM-DD format (e.g., 2024-12-31).")
        raise e