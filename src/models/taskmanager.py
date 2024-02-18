from .task import Task

class TaskManager:
    
    def __init__(self):
        self.tasks = []

    def add_task(self, task_text):
        task = Task(task_text)
        self.tasks.append(task)
    
    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.is_completed() else "Pending"
            print(f"{index + 1}. [{status}] {task.get_description()}")

    def mark_task_completed(self, task_index):
        if self.check_valid_task_index( task_index):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Invalid task index!")
        
    def delete_task(self, task_index):
        if self.check_valid_task_index(task_index):
            del self.tasks[task_index]
        else:
            print("Invalid task index!")

    def check_valid_task_index(self, task_index):
        if 0 <= task_index < len(self.tasks):
            return True
        else:
            return False
    
            
    