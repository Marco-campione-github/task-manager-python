from src.models.taskmanager import TaskManager

TaskManager = TaskManager()

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_description = input("Enter task description: ")
        TaskManager.add_task(task_description)
    elif choice == "2":
        TaskManager.view_tasks()
    elif choice == "3":
        task_index = int(input("Enter task index to mark as completed: ")) - 1
        TaskManager.mark_task_completed(task_index)
    elif choice == "4":
        task_index = int(input("Enter task index to delete: ")) - 1
        TaskManager.delete_task(task_index)
    elif choice == "5":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")