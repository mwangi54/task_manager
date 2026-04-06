# Import functions from task_manager package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

# Define the main function
def main():
    while True:
        print("\n" + "="*50)
        print("Task Management System")
        print("="*50)
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        print("-"*50)
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n--- Add New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            print("\n--- Mark Task as Complete ---")
            view_pending_tasks()
            try:
                index = input("\nEnter the task number to mark as complete: ")
                mark_task_as_complete(index)
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
        elif choice == "3":
            print("\n--- Viewing Pending Tasks ---")
            view_pending_tasks()
            
        elif choice == "4":
            print("\n--- Progress Report ---")
            progress = calculate_progress()
            print(f"\nOverall Progress: {progress:.1f}%")
            print(f"Completed: {progress:.1f}% | Remaining: {100-progress:.1f}%")
            
            # Visual progress bar
            bar_length = 50
            filled_length = int(bar_length * progress / 100)
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            print(f"\nProgress: [{bar}] {progress:.1f}%")
            
        elif choice == "5":
            print("\nExiting the program...")
            print("Thank you for using the Task Management System!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
            print("Please try again.")

if __name__ == "__main__":
    main()