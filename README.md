# Task Manager Application

This is a simple task manager application built with Python and PySide6. The application allows you to add, delete, and search tasks. It follows the Model-View-Controller (MVC) design pattern.

## Model-View-Controller (MVC)

The MVC pattern separates concerns into three components:

- Model: Handles data and related logic.
- View: Manages the user interface and presentation.
- Controller: Mediates between the model and view, handling application logic.
  ity Principle to maintain a clean and organized code structure.

The communication flow in this application is as follows:

- User interactions (like a button click) in the view trigger controller actions (like `add_task`).
- The controller manipulates the model (in this case, `TaskModel`) by adding tasks.
- The view updates its presentation based on the model's state.


## Code Snippets

Here's a brief look at how the MVC pattern is implemented in this application:

### Model

The `TaskModel` class represents the model. It stores a list of tasks and provides methods to manipulate the tasks.

```python
class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
```

### View

The TaskView class represents the view. It displays the user interface and handles user interactions.

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QMenu
from PySide6 import QtGui
from PySide6.QtCore import Qt


class TaskView(QWidget):
    """
    Represents the view component of the task management application.
    This class is responsible for displaying the user interface and handling user interactions.

    Args:
        controller (TaskController): The controller object responsible for handling task-related operations.
    """

    def __init__(self, controller): 
        """
        Initializes a new instance of the TaskView class.

        Args:
            controller (TaskController): The controller object responsible for handling task-related operations.
        """
        super().__init__() # Call the constructor of the parent class

        self.controller = controller # The view needs to access the controller to perform operations on tasks

        self.task_list = QListWidget() # A list widget to display the list of tasks
        self.task_input = QLineEdit() # A line edit widget to capture text for new tasks
        self.task_input.setPlaceholderText("Enter a task...") # Add a placeholder text to the input field
        self.add_button = QPushButton("Add Task") # A button to add tasks to the list
        self.add_button.setIcon(QtGui.QIcon('add_icon3.png')) # Add icons to the Add Task button and list items
        self.add_button.clicked.connect(self.add_task_clicked) # Connect the button click to the add_task_clicked method
        self.task_input.returnPressed.connect(self.add_task_clicked) # Connect the returnPressed signal to the add_task_clicked method
        self.clear_button = QPushButton("Clear List") #Add a button to clear the task list
        self.clear_button.clicked.connect(self.clear_task_list) # Connect the button click to the clear_task_list method
        self.task_list.setContextMenuPolicy(Qt.CustomContextMenu) # Set the context menu policy to custom
        self.task_list.customContextMenuRequested.connect(self.show_context_menu) # Connect the customContextMenuRequested signal to the show_context_menu method
        
        # Order button to toggle the order of the list
        self.order_button = QPushButton("Not Order") # Add a button to toggle the order of the list
        self.order_button.clicked.connect(self.toggle_order) # Connect the button click to the toggle_order method
        
        self.search_input = QLineEdit() # Add a line edit widget to capture text for searching tasks
        self.search_input.setPlaceholderText("Search...") # Add a placeholder text to the search input
        self.search_input.textChanged.connect(self.search_tasks) # Connect the textChanged signal to the search_tasks method
        
        
        self.setWindowIcon(QtGui.QIcon('icon5.png')) # add a icon to the window  
        self.setWindowTitle("Task Manager") # Set the window title

         # Apply stylesheets to make buttons and list prettier
        self.add_button.setStyleSheet(
            """QPushButton 
                { 
                    background-color: #4CAF50;
                    color: white; 
                    border: 1px solid #4CAF50;
                    padding: 5px;
                    border-radius: 300px;
                }
                
                QPushButton:hover 
                {
                    background-color: #4CAF10;
                    color: black;
                    border: 1px solid #4CAF50;
                    padding: 5px;
                }
                
                QPushButton:pressed {
                    background-color: #4CAF50;
                    color: white;
                    border: 1px solid #4CAF50;
                    padding: 5px;    
                 }""")
        
        self.task_list.setStyleSheet(
            """QListWidget 
                { 
                    background-color: #f2f2f2;
                    color: #333; 
                    border: 1px solid #4A4949;
                    padding: 5px; 
                } 
                
                QListWidget::item 
                {
                    border-bottom: 1px solid #4A4949;
                    padding: 5px;
                }
                
                QListWidget::item:selected
                {
                    background-color: #4CAF50;
                    color: white;
                }""")

        # Search-related widgets in a horizontal layout
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search")) # Add a label to the search layout
        search_layout.addWidget(self.search_input) # Add the search input to the search layout
        search_layout.addWidget(self.order_button) # Add the order button to the search layout

        # Main layout combining vertical layout and search-related layout
        layout = QVBoxLayout() 
        layout.addLayout(search_layout) # Add the search layout to the main layout
        layout.addWidget(self.task_list) # Add the task list to the main layout
        layout.addWidget(self.task_input) # Add the task input to the main layout
        layout.addWidget(self.add_button) # Add the add button to the main layout
        layout.addWidget(self.clear_button) # Add the clear button to the main layout
        
        self.setLayout(layout) # Use the layout for the window

    def toggle_order(self):
        """
        Toggles the order of the task list between "Not Order," "Asc," and "Dec."
        """
        current_text = self.order_button.text()
        if current_text == "Not Order": # If the current text is "Not Order"
            self.order_button.setText("Asc") # Set the text to "Asc"
            self.controller.sort_tasks(ascending=True) # Sort the tasks in ascending order
        elif current_text == "Asc": # If the current text is "Asc"
            self.order_button.setText("Dec") # Set the text to "Dec"
            self.controller.sort_tasks(ascending=False) # Sort the tasks in descending order
        elif current_text == "Dec": # If the current text is "Dec"
            self.order_button.setText("Asc") # Set the text to "Asc"
            self.controller.sort_tasks(ascending=True) # Sort the tasks in ascending order
        self.update_task_list()
        
    def search_tasks(self):
        """
        Search for tasks based on a keyword and display the filtered tasks in a list widget.

        Returns:
            None
        """
        keyword = self.search_input.text().lower() # Get the current text of the search input
        filtered_tasks = [task for task in self.controller.get_tasks() if keyword in task.lower()] # Filter the tasks based on the keyword
        self.task_list.clear() # Clear the list widget
        self.task_list.addItems(filtered_tasks) # Add the filtered tasks to the list widget

    def show_context_menu(self, pos):
        """
        Show a context menu at the given position.

        Parameters:
        - pos (QPoint): The position where the context menu should be shown.

        Returns:
            None
        """
        menu = QMenu(self) # Create a context menu
        delete_action = menu.addAction("Delete Task") # Add an option to delete the task
        action = menu.exec_(self.task_list.mapToGlobal(pos)) # Show the context menu

        if action == delete_action: # If the user selects the delete option
            selected_items = self.task_list.selectedItems() # Get the selected items
            for item in selected_items: # Iterate over the selected items
                self.controller.remove_task(item.text()) # Remove the task from the controller
                self.update_task_list() # Update the task list

    def add_task_clicked(self):
        """
        Event handler for the add task button click.
        Retrieves the task from the input field, adds it to the controller, and updates the task list.
        clears the input field at the end.
        """
        task = self.task_input.text() # Get the current text of the input field
        if task: # If the task is not an empty string
            self.controller.add_task(task) # Add the task to the controller
            self.update_task_list() # Update the task list
        self.task_input.setText("") # Clear the input field

    def update_task_list(self):
        """
        Updates the task list widget with the latest tasks from the controller.
        """
        self.task_list.clear() # Clear the list widget
        self.task_list.addItems(self.controller.get_tasks()) # Add the tasks to the list widget

    def clear_task_list(self):
        """
        Clears the task list in the controller and updates the task list.
        """
        self.controller.clear_task_list() # Clear the task list in the controller
        self.update_task_list() # Update the task list
```

### Controller

The TaskController class represents the controller. It handles the interaction between the model and the view.

```python
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
```
## Running the Application

To run the application, execute the main.py script:

```bash
python main.py
```
This will launch the task manager application. You can add tasks by typing into the input field and clicking the "Add Task" button. You can delete tasks by right-clicking on a task and selecting "Delete Task". You can search tasks by typing into the search field. You can also sort tasks in ascending or descending order by clicking the "Order" button.

## Dependencies

This application requires Python 3 and PySide6. You can install PySide6 with pip:

```python
pip install PySide6
```
## License

