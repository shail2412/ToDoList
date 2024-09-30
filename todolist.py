tasks = []

def addTask():
     task = input("please enter a task :")
     tasks.append(task)
     print(f"Task '{task}' added to the list.")

def listTasks():
  if not tasks:
     print("There are no Tasks currently:")  
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task#{index}.{task}")

def deleteTask():
    listTasks()
    try:
       taskToDelete = int(input("Enter the # to delete :"))
       if taskToDelete >=0 and taskToDelete < len(tasks):
        tasks.pop(taskToDelete)
        print(f"Task {taskToDelete} has been removed.")
       else :
        print(f"Task #{taskToDelete} was not found.")
    except:
       print("invalid input.")

if __name__ == "__main__":

    print("Welcome to the to do list:")
    while True:
        print("\n")
        print("Okyyy Just select one of the following options")
        print("----------------------------------------------")
        print("1. Add a new task")
        print("2. delete a task")
        print("3. list task")
        print("4. Quit")

        choice = input("Enter your choice:")
        if(choice == "1"):
             addTask()
        elif(choice == "2"):
             deleteTask()
        elif(choice == "3"):
             listTasks()
        elif(choice == "4"):
             break
        else:
             print("Invalid input. please try again.")
    print("Good byeeeeeeeee")


        



