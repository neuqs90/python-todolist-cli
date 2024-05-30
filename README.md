# To-Do List Application

## Overview
This is a simple command-line To-Do List application written in Python. It allows users to manage their tasks through a text-based menu interface. Users can add, update, delete, and clear tasks, and the tasks are saved to a file so they persist between program runs.

## Menu Options

1. **Add Task**: Prompt the user to enter a new task and add it to the list.
2. **Update Task**: Display current tasks and allow the user to update a selected task.
3. **Delete Task**: Display current tasks and allow the user to delete a selected task.
4. **Clear All Tasks**: Clear all tasks after confirming with the user.
5. **Exit**: Exit the program.

## How It Works
- Tasks are stored in a file named `tasks.txt`.
- The application loads tasks from this file when it starts and saves tasks to this file whenever changes are made.

## Usage

### Running the Application
1. Clone the repository:
    ```sh
    git clone https://github.com/neuqs90/python-todolist-cli.git
    cd python-todolist-cli
    ```
2. Ensure you have Python installed on your machine.
3. Run the application:
    ```sh
    python main.py
    ```

### Example Workflow
1. Upon running the application, a menu is displayed with options to add, update, delete, clear tasks, or exit.
2. Select an option by entering the corresponding number.
3. Follow the prompts to manage your tasks.
4. Tasks are automatically saved to `tasks.txt`.

## File Structure
- `main.py`: The main script containing the To-Do List application logic.
- `tasks.txt`: The file where tasks are stored.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request.
