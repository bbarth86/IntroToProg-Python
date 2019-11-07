# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Beau Barth,11.5.2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # A string that represents the ToDoList.txt file name
objFile = None  # An object that will represent the ToDoList.txt file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - Load current data in text file.
# Use a for loop to read each row in file, split the row into two
# values, and add values to task and priority keys into unique dictionaries, respectively.
# Append dictionaries to list.


objFile = open(strFile, "r")
for row in objFile:
    listRow = row.split(",")
    dicRow = {"task": listRow[0], "priority": listRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        taskInput = input("Enter a task: ")
        priorityInput = input("Enter a Priority for the task: ")
        dicRow = {"task": taskInput, "priority": priorityInput}  # assign task, priority values to new dictionary
        lstTable.append(dicRow)  # append new dictionary to list
        print("Task added successfully...\n")  # confirm addition
        continue

    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        taskQuery = input("Enter a task to remove: ")
        for item in lstTable:  # iterate over current list. for each item,
            if item["task"] == taskQuery:  # if value of task is equivalent to user input taskQuery
                lstTable.remove(item)  # remove the item dictionary from list
                print("Task successfully removed...")  # confirm removal
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        for row in lstTable:  # use for loop to append each row found in table list to ToDoList.txt
            objFile.write(row["task"] + "," + row["priority"] + "\n")
        objFile.close()
        print(strFile, "has been updated!")  # confirm update of text file
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Now Exiting the program...")  # confirm exit
        break  # and Exit the program
