
class TaskController:
    """
    The TaskController class handles the interaction between the model and the view.
    It provides methods to add tasks and retrieve the list of tasks.
    """

    def __init__(self, model, view):
        """
        Initializes a new instance of the TaskController class.

        Args:
            model (TaskModel): The task model.
            view (TaskView): The task view.
        """
        self.model = model # The controller needs to access the task list in the model
        self.view = view # The controller needs to access the task list in the view

    def add_task(self, task):
        """
        Adds a task to the model.

        Args:
            task (str): The task to be added.
        """
        self.model.add_task(task) # Add the task to the model

    def get_tasks(self):
        """
        Retrieves the list of tasks from the model.

        Returns:
            list: The list of tasks.
        """
        return self.model.tasks # Return a copy of the task list
    
    
    def clear_task_list(self):
        """
        Clears the task list in the model.
        """
        self.model.tasks.clear()
        
    def remove_task(self, task):
        """
        Removes a task from the model.

        Args:
            task: The task to be removed.

        Returns:
            None
        """
        self.model.tasks.remove(task) # Remove the task from the model
    
    def sort_tasks(self, ascending=None):
        """
        Sorts the tasks in the model.

        Args:
            ascending (bool): If set to True, sorts the tasks in ascending order. If set to False, sorts the tasks in descending order. If set to None, no sorting is applied.

        Returns:
            None
        """
        if ascending is not None:
            self.model.tasks.sort(reverse=not ascending) # Sort the tasks in ascending order

