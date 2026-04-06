from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    """Add a new task to the tasks list after validation."""
    try:
        # Validate all inputs
        validated_title = validate_task_title(title)
        validated_description = validate_task_description(description)
        validated_due_date = validate_due_date(due_date)
        
        # Create task dictionary
        task = {
            "title": validated_title,
            "description": validated_description,
            "due_date": validated_due_date,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add task to the list
        tasks.append(task)
        print("Task added successfully!")
        return True
    except ValueError as e:
        print(f"Error adding task: {e}")
        return False
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    """Mark a task as complete by its index."""
    try:
        # Convert to integer if needed
        index = int(index)
        
        # Check if index is valid
        if index < 0 or index >= len(tasks):
            print(f"Error: Invalid task index. Please enter a number between 0 and {len(tasks)-1}.")
            return False
        
        # Check if task is already completed
        if tasks[index]["completed"]:
            print(f"Task '{tasks[index]['title']}' is already marked as complete.")
            return False
        
        # Mark task as complete
        tasks[index]["completed"] = True
        tasks[index]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Task marked as complete!")
        return True
    except ValueError:
        print("Error: Please enter a valid number for the task index.")
        return False
    except Exception as e:
        print(f"Error marking task as complete: {e}")
        return False
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    """Display all pending (not completed) tasks."""
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    if not pending_tasks:
        print("\nNo pending tasks found!")
        print(f"Total tasks: {len(tasks)} | Completed: {len([t for t in tasks if t['completed']])}")
        return
    
    print("\n" + "="*80)
    print("PENDING TASKS")
    print("="*80)
    
    for idx, task in enumerate(tasks):
        if not task["completed"]:
            print(f"\nTask #{idx}")
            print(f"  Title: {task['title']}")
            print(f"  Description: {task['description'][:100]}{'...' if len(task['description']) > 100 else ''}")
            print(f"  Due Date: {task['due_date']}")
            print(f"  Created: {task['created_at']}")
            print("-"*40)
    
    print(f"\nTotal pending tasks: {len(pending_tasks)}")
    print(f"Total completed tasks: {len([t for t in tasks if t['completed']])}")
    print(f"Overall progress: {calculate_progress(tasks):.1f}%")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    """Calculate the percentage of completed tasks."""
    if not tasks:
        return 0.0
    
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / len(tasks)) * 100
    return progress