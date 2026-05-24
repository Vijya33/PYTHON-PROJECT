# TASK 1 : TO-DO LIST
# Python Project 1 - DecodeLabs

# List -> Full Database Table
task_list = []

# Primary Key
id = 1

while True:

    # OUTPUT (Display Menu)
    print("\n----- TO DO LIST ENGINE -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Exit")

    # INPUT (Data Entry)
    choice = input("Enter choice: ")

    # PROCESS : INSERT INTO
    if choice == "1":

        task_name = input("Enter task: ")

        # Dictionary -> Table Row
        row = {
            "id": id,
            "task": task_name
        }

        # INSERT INTO (list.append(row))
        task_list.append(row)

        print("Task stored in memory.")

        id = id + 1


    # OUTPUT : DISPLAY / VIEW
    elif choice == "2":

        if len(task_list) == 0:
            print("No tasks available.")

        else:
            print("\nTask Table:\n")

            for row in task_list:
                print("ID:", row["id"], " | Task:", row["task"])


    # SEARCH LOGIC
    elif choice == "3":

        search = input("Enter task keyword to search: ")

        found = False

        for row in task_list:
            if search.lower() in row["task"].lower():
                print("Found -> ID:", row["id"], "| Task:", row["task"])
                found = True

        if found == False:
            print("Task not found.")


    # EXIT PROGRAM
    elif choice == "4":

        print("Program closed.")
        break


    else:
        print("Invalid option.")