task = []
def addTask():
    tasks = input("Enter a Task: ")
    task.append(tasks)
    print(f"Task {tasks} added successfully")
def listTask():
    if not task:
         print("Task not found")
    else:
        print("Current Task!!")
        for index,tasks in enumerate(task):
            print(f"Task {index},{tasks}")
def deleteTask():
 addTask()
 try:
    taskToDelete = int(input("Enter Number To Delete: "))
    if taskToDelete >= 0 and taskToDelete < len(task):
        task.pop(taskToDelete)
        print(f"Task {taskToDelete} has been removed")
    else:
        print(f"Task {taskToDelete} has not found")
 except:
    print("Invalid Input")
if __name__ == "__main__":
    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Task")
        print("4. Quit")
        select = input("Enter a choice: ")
        if (select == "1"):
            addTask()
        elif (select == "2"):
            deleteTask()
        elif (select == "3"):
            listTask()
        elif (select == "4"):
            break        
        else:
            print("Invalid Input Try again")
print("Bye see you there!!")
