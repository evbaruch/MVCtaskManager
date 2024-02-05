class TaskModel:
    """
    Represents a task model that stores a list of tasks.
    """

    def __init__(self):
        """
        Initializes a new instance of the TaskModel class.
        """
        self.tasks = [] # A list of tasks

    def add_task(self, task):
        """
        Adds a task to the model.

        Args:
            task (str): The task to be added.
        """
        self.tasks.append(task) # Add the task to the list

