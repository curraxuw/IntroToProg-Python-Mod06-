# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Daniel Bretthauer,2020-08-17,Modified script to use functions):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# DanielB,2020-08-17,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "ToDoFile.txt"  # The name of the data file
file = None   # An object that represents a file
row = {}  # A row of data separated into elements of a dictionary {Task,Priority}
data = []  # A list that acts as a 'table' of rows
choice = ""  # Captures the user option selection
task = ""  # Captures the user task data
priority = ""  # Captures the user priority data
status = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod # Function that loads ToDoFile.txt.
    def read_data_from_file(file_name, data):
        data.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            row = line.split(",")
            row = {"Task": row[0].strip(), "Priority": row[1].strip()}
            data.append(row)
        file.close()
        return data, 'Success'

    @staticmethod # Function that adds a new item to the data table.
    def add_data_to_list(task, priority, data):
        row = {"Task": task, "Priority": priority}
        data.append(row)
        return data, 'Success'

    @staticmethod # Function that removes a task from the data table.
    def remove_data_from_list(task, data):
        bool_list = False
        for row in data:
            if row["Task"] == task:
                data.remove(row)
                bool_list = True
        if bool_list == False:
            print("I cannot find the task")
        return data, 'Success'

    @staticmethod # Function that writes data to file.
    def save_data_to_file(file_name, data):
        file = open(file_name, "w")
        for row in data:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        return data, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod # Function that displays a menu to the user.
    def print_menu_Tasks():
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod # Function that asks a user which menu option they will select.
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod # Function that displays current tasks/priorities to user.
    def print_current_Tasks_in_list(list_of_rows):
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod # Function that gets a yes or no from the user.
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

    @staticmethod # Function that causes program to pause before continuing.
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod # Function that gets user input for new task and priority.
    def input_new_task_and_priority():
        task = str(input("What is the task? - ")).lower().strip()
        priority = str(input("What is the priority? [high|low] - ")).lower().strip()
        return task, priority # return task, priority

    @staticmethod # Function that asks user which task should be removed.
    def input_task_to_remove():
        task = str(input("Which TASK would you like removed? - ")).lower().strip()
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name, data)  # read file data

# Step 2 - Display a menu of choices to the user
while(True): # Loop
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(data)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    choice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if choice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task, priority, data)
        IO.input_press_to_continue(status)
        continue  # to show the menu

    elif choice.strip() == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        Processor.remove_data_from_list(task, data)
        IO.input_press_to_continue(status)
        continue  # to show the menu

    elif choice.strip() == '3':   # Save Data to File
        choice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if choice.lower() == "y":
            Processor.save_data_to_file(file_name, data)
            IO.input_press_to_continue("Save Succeeded!")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif choice.strip() == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        choice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if choice.lower() == 'y':
            Processor.read_data_from_file(file_name, data)
            IO.input_press_to_continue(status)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif choice.strip() == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
