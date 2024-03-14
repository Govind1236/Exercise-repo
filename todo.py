task = []
def addTask():
    tasks = input("Enter a Task: ")
    task.append(tasks)
    print(f"Task {task} added to list")
def listTask():
    if not task:
        print("There is no task available currently")
    else:
        print("Current task:")
        for index,tasks in enumerate(task):
            print(f"Task {index}. {tasks}")
def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter number to delete: "))
        if taskToDelete >= 0 and  taskToDelete< len(task):
            task.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task {taskToDelete} is not found")
    except:
        print("Invalid Input")
if __name__ == "__main__":
# create a loop to run app
    print("Welcome to the TODO App")
while True:
    print("What will you like to do?")
    print("1. Add a task")
    print("2. Delete task")
    print("3. list task")
    print("4. Quit")

    choice = input("Enter your choice: ")
    if (choice == "1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif(choice == "3"):
        listTask()
    elif(choice == "4"):
        break
    else:
        print("Invalid input try again")
print("Bye")
    