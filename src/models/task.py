class Task:

    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def get_description(self):
        return self.description
    
    def is_completed(self):
        return self.completed