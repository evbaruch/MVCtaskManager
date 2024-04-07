import sys

from PySide6.QtWidgets import QApplication 

from TaskController import TaskController # Import the controller
from TaskModel import TaskModel # Import the model
from TaskView import TaskView # Import the view


## Separation of Concerns:

# Model: Handles data (tasks) and related logic.
# View: Manages the user interface and presentation.
# Controller: Mediates between the model and view, handling application logic.

## Single Responsibility Principle:

# Model: Responsible for managing the list of tasks.
# View: Responsible for presenting tasks and capturing user input.
# Controller: Responsible for coordinating actions between the model and view.

## Communication Flow:

# User interactions (button click) in the view trigger controller actions (add_task).
# Controller manipulates the model (TaskModel) by adding tasks.
# View updates its presentation based on the model's state.


def main():
    """
    Entry point of the application.
    Initializes the model, view, and controller.
    Shows the GUI and executes the application.
    """
    
    app = QApplication(sys.argv) # Create an instance of the application

    # model -> controller -> view -> controller -> model
    
    # model knows nothing about the view or controller (the model job is to store data and provide methods to manipulate the data)
    # view knows about the controller but not the model (the view job is to display the data and capture user input)
    # controller knows about both the model and view (the controller is the glue between the model and view)
    
    model = TaskModel() # Create a model
    view = TaskView(TaskController(model, None)) # Create a view and controller
    controller = TaskController(model, view) # Create a controller
    
    view.controller = controller  # Set the controller in the view (circular reference)

    view.show() # Show the GUI
    sys.exit(app.exec()) # Execute the application


if __name__ == "__main__":
         main()

