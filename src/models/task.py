from src.utils.helper_functions import check_date_format, check_date_not_past

class Task:

    # Set of priority levels
    PRIORITY_LEVELS = {'H', 'M', 'L'}

    def __init__(self, description, priority=None, due_to_date=None):

        self.description = description
        self.completed = False

        # Perform check on the priority if specified correctly as in PRIORITY_LEVELS
        if priority is not None:
            priority = priority.upper()
            if priority not in Task.PRIORITY_LEVELS or not isinstance(priority, str):
                raise ValueError("Priority must be one of 'H', 'M', or 'L'")
        self.priority = priority
        

        if due_to_date is not None:
            if not check_date_format(due_to_date):
                raise ValueError(f"{due_to_date} does not follow the 'YYYY-MM-DD' format.")
            if not check_date_not_past(due_to_date):
                raise ValueError(f"{due_to_date} is a past date.")
        self.due_to_date = due_to_date

    def mark_as_completed(self):
        self.completed = True

    def get_description(self):
        return self.description
    
    def get_priority(self):
        return self.priority
    
    def get_due_to_date(self):
        return self.due_to_date
    
    def is_completed(self):
        return self.completed
           
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        priority = self.priority if self.priority is not None else "Not set"
        due_to_date = self.due_to_date if self.due_to_date is not None else "Not set"
        return f"[status | {status}] [priority | {priority}] [due to | {due_to_date}] {self.description}"