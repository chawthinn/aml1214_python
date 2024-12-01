import os

# Initialize the class
class ToDoListManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = [] # Initialize an empty task list
        self.is_modified = False # Track whether tasks have been modified
        self.load_file() # load tasks from file if it exists

    # Define function to load file
    def load_file(self):
        """
        This is the function to load tasks from the file specified in self.filepath.
        Tasks are represented as dictionaires with keys 'description' and 'status'. 
        These dictionaries are stored in a list, which maintains the order of tasks as they are added.
        """
        print("Welcome to your To-Do List Manager!")

        try:
            # Load tasks from the file
            with open(self.filepath, "r") as file:
                self.tasks = []
                for line in file:
                    task_data = line.strip().split(" | ")
                    if len(task_data) == 2:
                        task, status = task_data
                        self.tasks.append({"description": task, "status": status})
                    else: 
                        print(f"Warning! Skipping broken line in the file: {line}")
            if not self.tasks:
                print("No tasks found in the file. Starting with an empty task list.")
            else:
                print("Tasks loaded successfully.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    # Define function to save tasks
    def save_tasks(self):
        """
        This is a function to save the current tasks to the file specified in self.filepath.
        Each task is stored in a dictionary with the following keys:
        - 'description': the task's name from user's input.
        - 'status': status of the task: 'completed' or 'pending'.
        These dictionaries are stored in a list, which maintains the order of tasks as they are added.
        """
        if self.is_modified:
            try:
                with open(self.filepath, "w") as file:
                    for task in self.tasks:
                        file.write(f"{task['description']} | {task['status']}\n")
                print(f"Tasks saved successfully to '{self.filepath}'.")
                self.is_modified = False  # Reset modified flag after tasks are saved
            except Exception as e: 
                print(f"Error saving tasks: {e}")
        else:
            print("No changes to save. Please make sure to modify the current tasks first.")

    # Define function to view tasks
    def view_tasks(self):
        """
        Displays all tasks in the current task list.
        The tasks are displayed in the order they were added to the list.
        Each task is represented by its 'description' and 'status'.
        """
        if not self.tasks:
            print("No tasks available. Please make sure to add tasks first. ")
        else:
            print("\nCurrent Tasks:")
            # Print headers according to max description length
            max_desc_len = max(len(task["description"]) for task in self.tasks)
            print(f"{'No.':<5} {'Description':<{max_desc_len}} {'Status':<10}")
            print("-" * (max_desc_len + 15))
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index:<5} {task['description']:<{max_desc_len}} {task['status']:<10}")

    # Define function to add tasks
    def add_task(self, description):
        """
        Adds a new task to the task list with a 'Pending' status.
        Parameters:
        - description (str): the description of the task to be added.
        After a task is added to the list with status "Pending", the modified flag is set to True, and the program will prompt a success message that the task is added.
        """
        self.tasks.append({"description": description, "status": "Pending"})
        self.is_modified = True 
        print(f"Success! Task '{description}' added.")
        print("To save this task to the file, please choose option 5 (Save Tasks).")

    # Define function to remove tasks
    def remove_task(self, index):
        """
        Remove a task from the task list based on its index.
        Parameters:
        - index (int): the index of the task to be removed.
        If the task index is valid, the task will be removed, and the modified flag will be set to True. Then, the program will prompt a success message that the task is removed.
        If the task index is invalid, the program will prompt an error message.
        """
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.is_modified = True
            print(f"Success! Task '{removed_task['description']}' removed.")
            print("To remove this task from the file, please choose option 5 (Save Tasks).")
        else:
            # Prompt error if invalid task number is chosen
            print("Error! Please choose a valid task number.")

    # Define function to mark tasks as completed
    def mark_task_completed(self, index):
        """
        Mark a task as 'Completed' based on its index.
        Parameters: 
        - index (int): the index of the task to be marked as 'Completed'.
        If the task index is valid, the task status will be updated to 'Completed', and the modified flag will be set to True. Then, the program will prompt a success message that the task is marked as completed.
        If the task index is invalid, the program will prompt an error message.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "Completed"
            self.is_modified = True
            print(f"Success! Task '{description}' marked as completed.")
            print("To save this status to the file, please choose option 5 (Save Tasks).")
        else:
            # Prompt error if invalid task number is chosen
            print("Error! Please choose a valid task number.")

    # Define function to quit application
    def quit_application(self):
        """
        Handle quitting the application, prompting the user to save unsaved modifications. 
        If there are unsaved changes, the program will prompt whether to save the tasks before quitting.
        If all changes are saved, the program will exist after saying 'Goodbye!'.
        Returns: 
        - bool: Returns 'True' if the program should quit, 'False' if returning to main menu
        """
        if self.is_modified:
            save_prompt = input("Warning! You have unsaved changes. Do you want to save your tasks before quitting? (y/n): ").strip().lower()
            if save_prompt == 'y':
                self.save_tasks()  
                print("Goodbye!")
                return True # Exit program after saving tasks
            elif save_prompt == 'n':
                print("Changes not saved. Goodbye!")
                return True # Exit program without saving
            else:
                print("Invalid input. Returning to main menu.")
                return False  # Return False to go back to the main menu
        else:
            print("Goodbye!")
            return True  # Exit the program if there are no unsaved changes

# Execute functions in Main Program
if __name__ == "__main__":

    # Define the file path for tasks.txt in the current directory
    file_path = "tasks.txt"

    # Chefk if the file exsits, and create it if not
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass  # Create an empty tasks.txt file

    # Initialize the ToDoListManager with a file path
    manager = ToDoListManager(filepath=file_path)

    while True:
        # Display our main menu
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Save Tasks")
        print("6. Reload Tasks from File")
        print("7. Quit")

        try:
            # Prompt user to input their choice of actions
            choice = int(input("Enter your choice: "))

            # Execute functions based on user choice of actions
            if choice == 1:
                # View all tasks
                manager.view_tasks()
            elif choice == 2:
                # Add a new task to the list
                description = input("Enter task description: ").strip()
                # Make sure that description is not empty
                while not description:
                    print("Task description cannot be empty. Please enter a valid description.")
                    description = input("Enter task description: ").strip()
                # Pass validated description to add_task function
                manager.add_task(description)              
            elif choice == 3:
                # Remove a task from the list
                manager.view_tasks() # Display current tasks for reference
                index = int(input("Enter task number to remove: ")) - 1 # -1 since we added 1 to index in the function
                manager.remove_task(index)
            elif choice == 4:
                # Mark a task as completed 
                manager.view_tasks()
                index = int(input("Enter task number to mark as completed: ")) - 1 
                manager.mark_task_completed(index)
            elif choice == 5:
                # Save the modified tasks to the tasks.txt 
                manager.save_tasks()
            elif choice == 6:
                # Reload tasks from the file, replacing the in-memory list
                manager.load_file()
            elif choice == 7:
                # Quit the application and prompt if there is any unsaved changes
                if manager.quit_application():
                    break # Exit the loop and terminate the program if true
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")
