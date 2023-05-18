# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a Python Dictionary.
#              Add each dictionary "row" to a Python list "table"
# ChangeLog (Who,When,What):Natta P., 05/17/2023
# RRoot,1.1.2030,Created started script
# <Natta P>,<05/17/23>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
lstTable = []  # A list that acts as a 'table' of rows

# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a Python list of dictionaries rows
try:
    objF = open(objFile, "r")
    for line in objF:
        no, task, status = line.strip().split(",")
        dicRow = {"No.": no, "To do :": task, "Status": status}
        lstTable.append(dicRow)
    objF.close()
except:
    print("No existing data in file.")

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

    strChoice = input("Which option would you like to perform? [1 to 5] - ")
    print("You choose:", strChoice)  # adding a new line for looks
    if (strChoice.lower() == 'exit'):
        break
    # Step 3 - Show the current items in the table
    elif strChoice.strip() == '1':
        if len(lstTable) == 0:
            print("Attention !!!: No any To do list, Good Job in keep up.")
        else:
            for dicRow in lstTable:
                print(dicRow)
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        no = int(input("Enter no.: "))
        task = str(input("Enter Task: "))
        status = str(input("Enter Status (Done, Ongoing, Not start): "))
        dicRow = {"No.": no, "To do :": task, "Status": status}
        lstTable.append(dicRow)
        print("Item added successfully!")

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        dropno = int(input("Enter no. you want to drop: "))
        found = False
        for dicRow in lstTable:
            if dicRow["No."] == dropno:
                lstTable.remove(dicRow)
                print("Item removed successfully!")
                found = True
                break
        if not found:
            print("No item with that number.")

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objF = open(objFile, "w")
        for dicRow in lstTable:
            objF.write(str(dicRow["No."]) + "," + dicRow["To do :"] + "," + dicRow["Status"] + "\n")
        objF.close()
        print("Data saved to file.")


    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program
