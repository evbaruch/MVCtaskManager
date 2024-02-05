# Task Manager Application

## Overview

The Task Manager application is a simple task management tool built using Python and the PySide6 library for the graphical user interface. The application follows the principles of Separation of Concerns and the Single Responsibility Principle to maintain a clean and organized code structure.

## Components

The application consists of three main components:

- Model (TaskModel): Manages the data, specifically the list of tasks, and provides methods to manipulate the data. The model is responsible for handling tasks' addition, removal, and sorting.

- View (TaskView): Manages the user interface and presentation. It displays the list of tasks, captures user input for new tasks, and provides buttons for various actions. The view communicates with the controller to perform operations on tasks.

- Controller (TaskController): Mediates between the model and view. It handles application logic, such as adding tasks, retrieving the list of tasks, clearing the task list, removing tasks, and sorting tasks. The controller ensures that the model and view remain decoupled.

## Features

The Task Manager application includes the following features:

- Add Task: Users can input tasks through the provided text field and add them to the task list.

- Remove Task: Users can select tasks from the list and delete them using the context menu.

- Clear Task List: Users can clear the entire task list using the "Clear List" button.

- Sort Tasks: Tasks can be sorted in ascending or descending order using the "Not Order," "Asc," and "Dec" toggle button.

- Search Tasks: Users can search for tasks by entering keywords in the search input field, and the displayed task list will be filtered accordingly.

## Usage

To run the application, execute the `main.py` file.

Follow these steps to use the Task Manager application:

1. Input tasks in the provided text field and press the "Add Task" button or press Enter.

2. Right-click on tasks in the list to access the context menu for task removal.

3. Use the "Clear List" button to remove all tasks from the list.

4. Toggle the order of the task list using the "Not Order," "Asc," and "Dec" buttons.

5. Search for specific tasks by entering keywords in the search input field.

## Styling

The application UI is styled for a more pleasant user experience, with customized button styles and a clean list presentation.

## Dependencies

- Python 3.x
- PySide6 library

## Acknowledgments

This project serves as a demonstration of basic principles in software architecture and graphical user interface design. Feel free to explore and modify the code for your learning and development purposes.
